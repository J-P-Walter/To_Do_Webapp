# Generated by Django 4.0.5 on 2022-06-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0004_alter_todolist_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
