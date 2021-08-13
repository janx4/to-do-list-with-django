from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True) 
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        ordering = ['created_time']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def __str__(self):
        return self.title

    