from django.shortcuts import render
from django.db.models import Q
from django.apps import apps
from games.models import Game

game = apps.get_model('games','Game')

# Create your views here.
def search_result(request):
    template = 'search/search_result.html'
    query = request.GET.get('search')
    if Game.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)):
        object_list = Game.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        results = len(object_list)
        context={'items': object_list, 'name':query, 'results':results}
        return render(request, template, context)

    #elif Game.objects.filter(description__icontains=query):
    #        object_list = Game.objects.filter((description__icontains=query) | )
    #        results = len(object_list)
    #        context={'items': object_list, 'name':query, 'results':results}
    #        return render(request, template, context)
    else:
        object_list = Game.objects.all()
        results = 0
        context={'items': object_list, 'name':query, 'results': results}
        return render(request, template, context)
