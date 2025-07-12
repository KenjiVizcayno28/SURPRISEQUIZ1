from django.db import models


# Create your models here.
class Projects(models.Model):
    name = models.CharField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
