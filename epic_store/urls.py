from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_games),
    path('games/', views.list_games),
    path('clear/', views.delete_games),
]
