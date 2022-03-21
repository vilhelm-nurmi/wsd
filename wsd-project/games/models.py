from django.db import models
import json
#Create your models here.
#Creating a game model
class Game(models.Model):
    #Adding describing title,description and a thumbnail picture
    uploader = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    #Dehär verkar lite cancer
    game_img = models.ImageField(upload_to='games/',null=True, blank=True,default="games/default.jpg")
    times_played= models.IntegerField(default=0)
    #Added a placeholder url where the game is hosted!
    url = models.URLField()
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=10.0)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Highscore(models.Model):
    game_h = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

class SavedGame(models.Model):
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    player = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    save_data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):

    user = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    pid = models.TextField()
    sid = models.TextField(default="miniclick123")
    secret_key = models.TextField()
    checksum = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    SUCCESS = 'S'
    ERROR = 'E'
    CANCEL = 'C'
    PENDING = 'P'
    STATUS_CHOICES = (
        (SUCCESS, 'Success'),
        (ERROR, 'Error'),
        (CANCEL, 'Cancel'),
        (PENDING, 'Pending'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    def __str__(self):
        time= "{}.{}.{} {}:{}".format(self.time_stamp.year,self.time_stamp.month,self.time_stamp.day,self.time_stamp.hour,self.time_stamp.minute)
        return "{} {} {} {}".format(self.user.username, self.game.title, time, self.status)
