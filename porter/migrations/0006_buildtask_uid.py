# Generated by Django 4.1.3 on 2022-12-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porter', '0005_buildtask_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildtask',
            name='uid',
            field=models.UUIDField(null=True),
        ),
    ]
