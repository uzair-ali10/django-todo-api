from django.core.exceptions import MiddlewareNotUsed
from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    priority = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    dueDate = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title