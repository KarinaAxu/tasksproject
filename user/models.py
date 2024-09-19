from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    avatar = models.ImageField(upload_to='user/', null=True, max_length=2000)
    bio = models.TextField(max_length=2000, null=False, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    tasks = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.id} {self.owner.first_name} {self.owner.last_name}'

    def teacher_display(self):
        if self.teacher:
            return f'Учитель: {self.teacher.first_name} {self.teacher.last_name}'
        else:
            return 'Учитель не указан'


class ResetPassword(models.Model):
    email = models.EmailField(null=False, blank=False, max_length=255)
    token = models.CharField(null=False, blank=False, max_length=255)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Reset Password'
        verbose_name_plural = 'Reset Passwords'

    def __str__(self):
        return f'{self.id} {self.email} {self.token} {self.created_at}'
