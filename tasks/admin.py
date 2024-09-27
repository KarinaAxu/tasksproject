from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'priority', 'category', 'due_date')
    list_filter = ('status', 'priority', 'category', 'user')

admin.site.register(Task, TaskAdmin)

def create_group():
    group = Group.objects.create(name='Project Manager')
    return group