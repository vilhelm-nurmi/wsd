from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.game_list, name = 'games'),
    path('add',views.add_game, name='add_game_form'),
    path('<str:link>', views.game_page, name ='game_page'),
    path('<str:link>/edit',views.edit_game, name='edit_game'),
    path('<str:link>/play',views.play_game, name='play_game'),
    path('<str:link>/highscores',views.highscores, name='highscores'),
    path('<str:link>/stats',views.stats_game, name='stats_game'),
]
