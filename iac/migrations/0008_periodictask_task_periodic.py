# Generated by Django 4.1.3 on 2022-11-19 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0016_alter_crontabschedule_timezone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iac', '0007_task_execute_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('playbook', models.CharField(default='site.yml', max_length=64)),
                ('inventories', models.TextField(default='')),
                ('envvars', models.TextField(default='')),
                ('extravars', models.TextField(default='')),
                ('uid', models.UUIDField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('periodic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_celery_beat.periodictask')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iac.repository')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='task',
            name='periodic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='iac.periodictask'),
        ),
    ]
