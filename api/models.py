from django.db import models

class Habitat(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=40)
    sound = models.CharField(max_length=15)
    desc = models.TextField(max_length=200)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name