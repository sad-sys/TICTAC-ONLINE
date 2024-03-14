from django.contrib import admin

# Register your models here.
from .models import gameSession  # Import your model

admin.site.register(gameSession)