from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_games),
    path('games/', views.list_games),
    path('game/', views.get_game),
    path('clear/', views.delete_games),
]
