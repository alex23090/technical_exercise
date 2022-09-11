from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    age = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    games = models.ManyToManyField('Game', blank=True)

    def __str__(self):
        return str(self.name)


class Game(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)
