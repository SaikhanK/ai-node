from django.db import models

class Task(models.Model):
    title = models.CharField()
    description = models.CharField()

 