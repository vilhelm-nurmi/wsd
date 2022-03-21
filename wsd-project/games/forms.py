from .models import Game
from django import forms

class GameForm(forms.ModelForm):
    class Meta:
        model= Game
        fields=('title','slug','description','game_img','url','price',)

class GameForm2(forms.ModelForm):
    class Meta:
        model= Game
        fields=('title','slug','description','game_img','url','price',)
