# Generated by Django 4.1.3 on 2022-11-19 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iac', '0005_task_envvars_task_extravars_task_inventories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='RunnerEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=256)),
                ('changed', models.BooleanField(null=True)),
                ('playbook', models.CharField(max_length=64)),
                ('playbook_uuid', models.UUIDField()),
                ('play', models.CharField(max_length=255)),
                ('play_uuid', models.UUIDField()),
                ('task_name', models.CharField(max_length=255)),
                ('task_uuid', models.UUIDField()),
                ('remote_addr', models.GenericIPAddressField(null=True)),
                ('state', models.IntegerField(choices=[(0, 'PENDING'), (1, 'RUNNING'), (2, 'COMPLETED'), (3, 'FAILED'), (4, 'CANCELED'), (5, 'TIMEOUT'), (6, 'CANCELING')], default=1)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('duration', models.FloatField(default=0)),
                ('res', models.JSONField(null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iac.task')),
            ],
            options={
                'unique_together': {('task_id', 'host', 'playbook_uuid', 'play_uuid', 'task_uuid')},
            },
        ),
    ]
