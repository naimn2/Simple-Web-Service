from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=70)
    desc = models.TextField()

    def __str__(self):
        return self.name
    