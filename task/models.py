from django.db import models
from app import manager
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=50, null=True)
    completed = models.BooleanField(default=False, blank=True)
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.title