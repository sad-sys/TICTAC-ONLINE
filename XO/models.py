from django.db import models

class gameSession(models.Model):
    gameCode = models.CharField(max_length = 8)
    userTurn = models.CharField(max_length = 8)
    gameState = models.CharField(max_length = 8)
    xArr = models.JSONField(default = list)
    oArr = models.JSONField(default = list)
