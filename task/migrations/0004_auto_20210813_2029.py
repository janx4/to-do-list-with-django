# Generated by Django 3.2.4 on 2021-08-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_taskmodel_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskmodel',
            options={'ordering': ['created_time'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]