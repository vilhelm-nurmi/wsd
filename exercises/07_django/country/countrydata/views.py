from django.http import Http404, HttpResponse, JsonResponse
import json
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Continent, Country
from django.forms.models import model_to_dict

def continent_json(request, continent_code):
    a = get_object_or_404(Continent, code = continent_code)
    countries = get_list_or_404(Country, continent = a)
    palaut = {i['code']: i['name'] for i in  [model_to_dict(country, fields = ['name', 'code']) for country in countries]}
    if 'callback' in request.GET:
        data = json.dumps(palaut)
        data = "{}({})".format(request.GET['callback'],data)
        return HttpResponse(data, 'text/javascript')
    return JsonResponse(palaut)


def country_json(request, continent_code, country_code):
    continent = get_object_or_404(Continent, code = continent_code)
    count = get_object_or_404(Country, continent = continent, code = country_code)
    if 'callback' in request.GET:
        data = json.dumps(model_to_dict(count, fields = ["area", "population", "capital"]))
        data = "{}({})".format(request.GET["callback"], data)
        return HttpResponse(data, 'text/javascript')
    return JsonResponse( model_to_dict(count, fields = ["area", "population", "capital"]))