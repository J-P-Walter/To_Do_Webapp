# Generated by Django 4.0.5 on 2022-06-22 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0003_alter_todolist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(default=datetime.date(2022, 6, 22)),
        ),
    ]