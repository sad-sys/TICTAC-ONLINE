from django.contrib import admin

# Register your models here.
from .models import GameSession  # Import your model

admin.site.register(GameSession)