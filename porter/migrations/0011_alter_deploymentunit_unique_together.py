# Generated by Django 4.1.3 on 2023-01-02 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porter', '0010_alter_lane_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='deploymentunit',
            unique_together={('project', 'cluster', 'namespace')},
        ),
    ]
