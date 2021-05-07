from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(User, related_name='todos',
                             on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(
        default=datetime.today() + timedelta(days=2))
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
