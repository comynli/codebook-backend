import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codebook.settings')

app = Celery('codebook')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def hello_beat():
    print("beat.....")

