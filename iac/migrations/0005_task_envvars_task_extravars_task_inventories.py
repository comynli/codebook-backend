# Generated by Django 4.1.3 on 2022-11-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iac', '0004_alter_repository_options_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='envvars',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='extravars',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='inventories',
            field=models.TextField(default=''),
        ),
    ]
