""" Views """
from django.http import HttpResponse
from django.shortcuts import render
from games.models import Game

def homepage(request):
    #return HttpResponse('homepage')
    games = Game.objects.all().order_by('-times_played')
    return render(request,"homepage.html",{'games':games})
def toplist(request):
    #return HttpResponse('toplist')
    games = Game.objects.all().order_by('-times_played')
    return render(request,"toplist.html", {'games':games})

def complaints(request):
    return render(request,"complaints.html")
