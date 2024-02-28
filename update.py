import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'battleship.settings')

django.setup()
from mainGame.models import GameSession

# Update the 'my_field' column for all records in MyModel
GameSession.objects.all().update(gameState = 1)