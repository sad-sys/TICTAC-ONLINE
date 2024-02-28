from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import json

from .forms import CodeForm
from .models import GameSession

import datetime
import random
import string

issued_codes = set()  

'Makes the game Code is used in the makeCode function below'
def game_codeCode():
    now = datetime.datetime.now()
    random_part = random.choice(string.ascii_uppercase)
    second = str(now.second) 
    game_code = random_part  + second
    return game_code

'Uses make code HTML to generate a user Code, then creates a corresponding gameSession object'
def makeCode(request):
    game_code = game_codeCode()
    while GameSession.objects.filter(game_code=game_code).exists():
        game_code = game_codeCode()

    # Create a new game session with this unique code
    game_sessionPlayer = GameSession(game_code=game_code,
                                      playerXArr=[[0,0,0],[0,0,0],[0,0,0]], 
                                      playerOArr=[[0,0,0],[0,0,0],[0,0,0]],
                                      gameState=False)  # Assuming empty players initially
    game_sessionPlayer.save()
    specificPlayer = GameSession.objects.get(game_code=game_code)
    game_code = specificPlayer.game_code
    gameState = specificPlayer.gameState
    playerXarr = specificPlayer.playerXArr
    playerOarr = specificPlayer.playerOArr
    form = CodeForm(request.POST)
    context = \
    {
        'form': form,  # Form instance
        'game_code': game_code,
        'gameState':gameState,
        'playerXarr': playerXarr,
        'playerOarr': playerOarr
    }
    return render(request, 'mainGame/makeCode.html', context,)

def joinAsChallenger(request):
    # Use request.POST.get if game_code is sent in a POST request
    game_code = request.POST.get('game_code')
    exists = GameSession.objects.filter(game_code=game_code).exists()

    if exists:
        specificPlayer = GameSession.objects.get(game_code=game_code)
        # Update gameState or other fields as needed
        specificPlayer.gameState = True
        specificPlayer.save()
        game_code = specificPlayer.game_code
        # Prepare context with existing game session details
        context = \
        {
            'form': CodeForm(),  # Assuming you need a blank form here; adjust as needed
            'game_code': specificPlayer.game_code,
            'gameState': specificPlayer.gameState,
            'playerXarr': specificPlayer.playerXArr,
            'playerOarr': specificPlayer.playerOArr
        }
        print("Exists")
    else:
        print("Doesn't exist")
        context = {'game_code': "Doesn't exist please go back and try again"}

    print("Game state is ", specificPlayer.gameState if exists else "N/A")
    return render(request, 'mainGame/gamePageXChallenger.html', context)

def checkGameState(request):
    game_code = request.GET.get('game_code', '').strip()
    print("Game Code is",game_code)
    specificPlayer = GameSession.objects.get(game_code=game_code)
    game_state = specificPlayer.gameState
    game_state = {"gameState":game_state}  # Example response, add other necessary game state information
    print (game_state)
    if game_state == 1:
        return render(request, 'gamePageXChallenger.html')
    else:
        return JsonResponse(game_state)

def joinAsOpponent(request):
    if request.method == 'POST':
        game_code = request.POST.get('game_code', '').strip()
    else:
        # Handle the case for a GET request or other methods if needed
        game_code = request.GET.get('game_code', '').strip()
    # Fetch the game session using the game code
    specificPlayer = GameSession.objects.get(game_code=game_code)
    context = \
    {
        'form': CodeForm(),  # Assuming you need a blank form here; adjust as needed
        'game_code': specificPlayer.game_code,
        'game_state': specificPlayer.gameState,
        'playerXarr': specificPlayer.playerXArr,
        'playerOarr': specificPlayer.playerOArr
    }
    # Render the template for the opponent, passing the context
    return render(request, 'mainGame/gamePageOChallenger.html', context)

def checkGamePiece(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dataToSend = data.get('dataToSend')
        print("POST", dataToSend)
        # Process your data here
        return JsonResponse({'status': 'success', 'data': dataToSend})