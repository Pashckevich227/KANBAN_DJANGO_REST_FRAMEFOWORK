# Generated by Django 4.1.7 on 2023-06-01 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_app', '0003_alter_category_color_alter_task_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
