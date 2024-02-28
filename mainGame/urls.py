from django.urls import path

from . import views

urlpatterns = [
    path("makeCode", views.makeCode, name="code"),
    path("joinAsChallenger", views.joinAsChallenger, name="joinAsChallenger"),
    path("joinAsOpponent", views.joinAsOpponent, name = "joinAsOpponent"),
    path("checkGameState", views.checkGameState, name="checkGameState" ),
    path("checkGamePiece", views.checkGamePiece, name="checkGamePiece")
]