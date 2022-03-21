from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.db import models
from .forms import CustomUserCreationForm, CustomUserChangeForm
from games.models import Game
from django.contrib.auth.models import Group

class CustomUserAdmin(admin.ModelAdmin):
    fields = ('username','first_name','last_name','email','verified','type','purchased_games','profile_img')
    purchased_games = models.ManyToManyField(Game)
    list_display = ['username','email','first_name','last_name','type']
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.site_header= "Miniclick admin area"
#admin.site.register(CustomUser,UserAdmin)
