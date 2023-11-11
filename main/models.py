from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE
        )