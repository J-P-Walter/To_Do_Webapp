# Generated by Django 4.0.5 on 2022-06-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0002_alter_todolist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(null=True),
        ),
    ]