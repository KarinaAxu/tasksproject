from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('NS', 'Not Started'),
        ('IP', 'In Progress'),
        ('CO', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    CATEGORY_CHOICES = [
        ('W', 'Work'),
        ('P', 'Personal'),
        ('U', 'Urgent'),
    ]

    title = models.CharField(max_length=255, default='')
    description = models.TextField(max_length=10000, default='', blank=True)
    due_date = models.DateField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NS')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='P')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f'{self.title} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'