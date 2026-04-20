# card/models.py
from django.db import models
from django.contrib.auth.models import User
class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.URLField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    