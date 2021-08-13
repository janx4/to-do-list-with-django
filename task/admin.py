from django.contrib import admin
from .models import TaskModel


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}
    

admin.site.register(TaskModel, TaskAdmin)