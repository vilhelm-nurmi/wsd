from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length = 255, unique = True, blank = False)
    code = models.CharField(max_length = 255, unique = True, blank = False)
    class Meta:
        ordering = ["name"]


class Country(models.Model):
    name = models.CharField(max_length = 255, unique = True, blank = False)
    capital = models.CharField(max_length = 255, blank = False)
    population = models.PositiveIntegerField(default = 0)
    area = models.PositiveIntegerField(default = 0)
    code = models.CharField(max_length = 255, unique = True, blank = False)
    continent = models.ForeignKey(Continent, on_delete = models.CASCADE, related_name = "countries")
    class Meta:
	    ordering = ["name"]
