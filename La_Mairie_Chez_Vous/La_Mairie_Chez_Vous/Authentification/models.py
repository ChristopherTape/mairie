from django.db import models
from django.contrib.auth.models import User, AbstractUser

class CustomUser(AbstractUser):
    is_agent=models.BooleanField(default=False)


class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)
    nom =models.CharField(max_length=50)
    mairie = models.CharField(max_length=50, default='Cocody')
    num = models.CharField(max_length=50, default='0160756069')

    def __str__(self) -> str:
        return f"{self.mairie}"




