from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.db import models
from games.models import Game
class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
        'class':'form-control x-auto',
        'placeholder':'Create a username'}))

    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
        'class':'form-control x-auto',
        'placeholder':'First Name'}))

    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
        'class':'form-control x-auto ',
        'placeholder':'Last Name'}))

    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={
        'class':'form-control ',
        'placeholder':'E-mail'}))

    ACCOUNT_CHOICES = (('P','Player'),('D','Developer',))
    type = forms.ChoiceField(label='',choices=ACCOUNT_CHOICES,widget=forms.RadioSelect(
    ))


    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name', 'email', 'type','profile_img')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields = ('username','first_name','last_name','email','profile_img')

class EditProfile(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)
        del self.fields['password']
    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name','profile_img')
