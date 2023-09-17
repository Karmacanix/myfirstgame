from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=60) 
    NUMBER_OF_PLAYER_CHOICES = [
        ("2", "2 players"),        
        ("4", "4 players"),
        ("6", "6 players"),
        ("8", "8 players"),
    ]
    number_of_players = models.CharField(
        max_length=1,
        choices=NUMBER_OF_PLAYER_CHOICES,
        default="4",
        help_text="Select number of players:",
    )
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return f"/game/{self.pk}/"
    
    def __str__(self):
        return self.name
    


class GamePlayers(models.Model):
    player = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    turn_order = models.PositiveSmallIntegerField(null=True)
    
    class Meta:
        unique_together = [["player", "game"]]


class GameRound (models.Model):
    pass

