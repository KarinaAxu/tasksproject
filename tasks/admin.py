from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'priority', 'category', 'due_date')
    list_filter = ('status', 'priority', 'category', 'user')

admin.site.register(Task, TaskAdmin)