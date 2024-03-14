from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import json

from .forms import CodeForm
from .models import gameSession

import datetime
import random
import string

'This function makes the code that is used for each gameSession'
def gameCodeMaker():
    now = datetime.datetime.now()
    randomLetter = random.choice(string.ascii_uppercase)
    second = str(now.second)
    gameCode = randomLetter + second
    return gameCode

'''
class gameSession(models.Model):
    gameCode = models.CharField(max_length = 8)
    userTurn = models.CharField(max_length = 8)
    gameState = models.CharField(max_length = 8)
    xArr = models.JSONField(default = list)
    oArr = models.JSONField(default = list)
'''

'HomePage makes the gameSession and the corresponding gameCode, which if inputted goes to a specific page'

def index(request):
    gameCode = gameCodeMaker()
    gameSessionObject = gameSession(gameCode = gameCode,
                                    userTurn = 0,
                                    gameState = 0,
                                    xArr = [[0,0,0],[0,0,0],[0,0,0]],
                                    oArr = [[0,0,0],[0,0,0],[0,0,0]])
    gameSessionObject.save()
    specificPlayer = gameSession.objects.get(gameCode = gameCode)
    gameCode = specificPlayer.gameCode
    userTurn = specificPlayer.userTurn
    gameState = specificPlayer.gameState
    xArr = specificPlayer.xArr
    oArr = specificPlayer.oArr

    gameSessionContext = \
    {
        'gameCode': gameCode,
        'userTurn' : userTurn,
        'gameState': gameState,
        'xArr' : xArr,
        'oArr' : oArr,
        'form': CodeForm,
    }
    print("Got Game Object")
    return render(request, '/Users/sadiqkhawaja/Desktop/Brackets/Battleship2/battleship2/XO/templates/XO/homePage.html', gameSessionContext)

'When the form is put in it triggers the Opponent homescreen where people can put into HomeScreen '
def joinAsOOpponent(request):
    gameCode = request.POST.get('gameCodeInput', '').strip()
    print ("Game Code is inputted", gameCode)
    try:
        specificPlayer = gameSession.objects.get(gameCode = gameCode)
    except:
        print ("NOT FOUND " * 100)
        gameCode = gameCodeMaker()
        gameSessionObject = gameSession(gameCode = gameCode,
                                        userTurn = 0,
                                        gameState = 0,
                                        xArr = [[0,0,0],[0,0,0],[0,0,0]],
                                        oArr = [[0,0,0],[0,0,0],[0,0,0]])
        gameSessionObject.save()
        specificPlayer = gameSession.objects.get(gameCode = gameCode)
        gameCode = specificPlayer.gameCode
        userTurn = specificPlayer.userTurn
        gameState = specificPlayer.gameState
        xArr = specificPlayer.xArr
        oArr = specificPlayer.oArr

        gameSessionContext = \
        {
            'gameCode': gameCode,
            'userTurn' : userTurn,
            'gameState': gameState,
            'xArr' : xArr,
            'oArr' : oArr,
            'form': CodeForm,
        }
        print("Got Game Object")
        return render(request, '/Users/sadiqkhawaja/Desktop/Brackets/Battleship2/battleship2/XO/templates/XO/homePage.html', gameSessionContext)
    
    gameCode = specificPlayer.gameCode
    userTurn = specificPlayer.userTurn
    gameState = specificPlayer.gameState
    xArr = specificPlayer.xArr
    oArr = specificPlayer.oArr

    gameSessionContextForO = \
    {
        'gameCode': gameCode,
        'userTurn' : userTurn,
        'gameState': gameState,
        'xArr' : xArr,
        'oArr' : oArr,
        'form': CodeForm,
    }
    return render(request, '/Users/sadiqkhawaja/Desktop/Brackets/Battleship2/battleship2/XO/templates/XO/opponent.html', gameSessionContextForO)

'Turning the Input into the oArr'
def changeOrrOpponent(request):
    pass