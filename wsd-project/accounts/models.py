from django.db import models
from django.contrib.auth.models import AbstractUser
from games.models import Game
from django import forms
import random
# Adding on to the base AbstractUser
class CustomUser(AbstractUser):

    #ManyToManyField that links users to purchased games
    purchased_games = models.ManyToManyField(Game, blank=True)

    #Verified
    verified = models.BooleanField(default=False)
    personalvar = random.randint(1000000,9999999)
    personal_secret_key = models.IntegerField( default=personalvar )


    #Adding a type of account
    ACCOUNT_CHOICES = (
        ('P','Player'),
        ('D','Developer'),
        )

    type= models.CharField(max_length=1, choices=ACCOUNT_CHOICES, default='P')
    profile_img=models.ImageField(upload_to='usr/',null=True, blank=True, default="usr/default.png")
    def __str__(self):
        return self.username
    def get_purchased_games_titles(self):
        list=[]
        for x in self.purchased_games.all():
            list.append(x.title)
        return list
