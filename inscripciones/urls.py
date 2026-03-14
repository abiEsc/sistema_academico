from django.urls import path
from .views import quiz_view
from .views import quiz_view, memory_game 
from . import views
urlpatterns = [
    path("quiz/", quiz_view, name="quiz"),
    path("memory/", memory_game, name="memory_game"),
    path("mapa/", views.map_view, name="mapa"),
    path("verse_cards/", views.verse_cards, name="verse_cards"),
    path("menu/", views.menu_view, name="menu"),
    path("general_quiz/", views.general_quiz_view, name="general_quiz"),
]
