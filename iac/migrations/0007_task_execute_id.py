# Generated by Django 4.1.3 on 2022-11-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iac', '0006_alter_task_options_runnerevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='execute_id',
            field=models.UUIDField(null=True),
        ),
    ]
