from django.urls import path
from .views import quiz_view
from .views import quiz_view, memory_game 
from . import views
urlpatterns = [
    path("quiz/", quiz_view, name="quiz"),
    path("memory/", memory_game, name="memory_game"),
    path("mapa/", views.map_view, name="mapa"),
]
