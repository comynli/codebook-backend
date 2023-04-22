from typing import List

from ..models import Project, Pipeline, Stage, DeploymentUnit, TaskState, DeployTask
from ..tasks import submit_deploy_task


class PipelineRunner:
    # 开始一个Pipeline
    @classmethod
    def start(cls, project: Project, version: str, user) -> Pipeline:
        pipeline = Pipeline.objects.filter(project=project, version=version).first()
        if pipeline is not None:
            return pipeline
        return Pipeline.objects.create(project=project, version=version, created_by=user, updated_by=user)

    @classmethod
    def _get_next(cls, project: Project, stage: Stage, index: int):
        if stage is None:
            return []
        if stage.strict:
            lane = stage.lane_set.filter(index__gt=index).order_by("index").first()
            if lane is None:
                stage = Stage.objects.filter(index__gt=stage.index).first()
                return cls._get_next(project, stage, -1)
            return DeploymentUnit.objects.filter(project=project, lane=lane).all()
        else:
            res = []
            units = DeploymentUnit.objects.filter(project=project, stage=stage, lane__index__gt=index).all()
            res.extend(units)
            if index >= 0 or len(res) <= 0:
                stage = Stage.objects.filter(index__gt=stage.index).first()
                res.extend(cls._get_next(project, stage, -1))
            return res

    # 返回下一步可执行的deployment unit 列表
    @classmethod
    def next(cls, pipeline: Pipeline) -> List[DeploymentUnit]:
        if pipeline.closed:
            return []
        if pipeline.current is None:
            stage = Stage.objects.order_by("index").first()
            return cls._get_next(pipeline.project, stage, -1)
        if pipeline.current.state != TaskState.COMPLETED:
            return [pipeline.current.deployment_unit]
        stage = pipeline.current.deployment_unit.stage
        return cls._get_next(pipeline.project, stage, pipeline.current.deployment_unit.lane.index)

    # 执行发布 如果unit id 为空，则重新执行当前步骤
    @classmethod
    def execute(cls, pipeline: Pipeline, user, unit_id: int = None):
        if pipeline.closed:
            return pipeline
        if unit_id is None:
            if pipeline.current is None:
                raise Exception()
            if pipeline.current.state == TaskState.PENDING:
                submit_deploy_task.delay(pipeline.current.id)
                return pipeline
            if pipeline.current.state == TaskState.RUNNING:
                return pipeline
            pipeline.current = DeployTask.objects.create(
                deployment_unit=pipeline.current.deployment_unit,
                version=pipeline.version,
                pipeline=pipeline,
                created_by=user,
                updated_by=user
            )
            submit_deploy_task.delay(pipeline.current.id)
            return pipeline
        if pipeline.current is not None and pipeline.current.state != TaskState.COMPLETED:
            raise Exception("invalid state")
        units = cls.next(pipeline)
        for unit in units:
            if unit.id == unit_id:
                pipeline.current = DeployTask.objects.create(
                    deployment_unit=unit,
                    version=pipeline.version,
                    pipeline=pipeline,
                    created_by=user,
                    updated_by=user
                )
                submit_deploy_task.delay(pipeline.current.id)
                pipeline.save()
                return pipeline
        raise Exception("invalid deployment unit")

    # 关闭当前pipeline
    @classmethod
    def close(cls, pipeline, user):
        if pipeline.current is None or pipeline.current.state not in {TaskState.RUNNING, TaskState.PENDING}:
            pipeline.closed = True
            pipeline.updated_by = user
            pipeline.save()
            return pipeline
        raise Exception("invalid state")
