from django.db import models

# Create your models here.
class GameSession(models.Model):
    game_code = models.CharField(max_length = 3)
    playerXArr = models.JSONField(default = list) #Challenger
    playerOArr = models.JSONField(default = list) #ODefender
    gameState = models.IntegerField(null=True, blank=True, default = 0)
    numberOfMoves = models.IntegerField(blank=True, default = 0)
    gameTurn = models.IntegerField(null=True,default = 0)
    playerTurn = models.IntegerField(null=True,default=0)