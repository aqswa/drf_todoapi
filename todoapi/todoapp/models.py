from django.db import models
from django.forms import BooleanField, CharField, DateTimeField

# Create your models here.


class Todo(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    content = models.CharField(default="", max_length=100)
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ['start_time']
