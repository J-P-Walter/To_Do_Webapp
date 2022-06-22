from django.db import models
import datetime

# Create your models here.
class ToDoList(models.Model):
    #Put in "completed field, false default"
    title       = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=False, default='')
    date        = models.DateField(default=datetime.datetime.now().date()) #maybe change this?
    done        = models.BooleanField(default=False)
