from django import forms
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to' , 'status', 'priority', 'category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.groups.filter(name='Project Manager').exists():
            self.fields['assigned_to'].queryset = User.objects.all()
        else:
            self.fields['assigned_to'].queryset = User.objects.filter()