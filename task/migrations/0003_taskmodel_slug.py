# Generated by Django 3.2.4 on 2021-08-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_task_taskmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
