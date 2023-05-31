from django.db import models
from django.contrib.auth.models import User

class users(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    telegram_id = models.IntegerField(null=True)
