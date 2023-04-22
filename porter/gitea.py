from collections import OrderedDict
from urllib.parse import urlparse
from datetime import datetime

from gitea.api.repository_api import RepositoryApi
from gitea.configuration import Configuration
from gitea.api_client import ApiClient
from gitea.model.commit import Commit
from .models import Commit as CommitModel
from .serializers import CommitSerializer


class GiteaClient:
    def __init__(self, base, token):
        self.configuration = Configuration(
            host=base,
            api_key={"AuthorizationHeaderToken": token},
            api_key_prefix={"AuthorizationHeaderToken": "token"}
        )

    @property
    def client(self):
        return ApiClient(self.configuration)

    @property
    def repository_api(self):
        return RepositoryApi(self.client)

    def _parse(self, repository):
        owner, repo = urlparse(repository).path.strip("/").split("/", maxsplit=2)
        return owner, repo.removesuffix(".git")

    @staticmethod
    def _commit_to_model(commit: Commit) -> CommitModel:
        model = CommitModel()
        model.sha = commit.sha
        model.url = commit.html_url
        model.message = commit.commit.get("message")
        committer = commit.commit.get("committer")
        model.committer_name = committer.get("name")
        model.committer_email = committer.get("email")
        model.committed_at = datetime.fromisoformat(committer.get("date").replace('Z', '+00:00'))
        return model

    def save(self, commit: CommitModel):
        exist = CommitModel.objects.filter(sha=commit.sha).first()
        if exist is not None:
            return exist
        commit.save()
        return commit

    def get_commit(self, repository, sha) -> CommitModel:
        owner, repo = self._parse(repository)
        commit = self.repository_api.repo_get_single_commit(owner, repo, sha, _check_return_type=False)
        return self._commit_to_model(commit)

    def list_commit(self, repository, page, size):
        owner, repo = self._parse(repository)
        commits, _, headers = self.repository_api.repo_get_all_commits(owner, repo, page=page, limit=size,
                                                                       _check_return_type=False,
                                                                       _return_http_data_only=False)

        return OrderedDict([
            ('count', int(headers.get("x-total"))),
            ('current', int(headers.get("x-page"))),
            ('size', int(headers.get("x-perpage"))),
            ('results', (CommitSerializer(self._commit_to_model(x)).data for x in commits))
        ])
