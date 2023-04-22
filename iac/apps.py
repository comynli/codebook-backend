from django.apps import AppConfig


class IacConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iac'

    # def ready(self):
    #     super(IacConfig, self).ready()
    #     from .views import TaskViewSet
    #     from .runner import Runner
    #     runner = Runner()
    #     threading.Thread(target=runner.start).start()
    #     TaskViewSet.runner = runner
