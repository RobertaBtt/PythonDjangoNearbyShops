from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
#from django.contrib.gis.utils import GeoIP


# Create your views here.wagtail start

latitude = 39.2204288
longitude = 9.1203738

#39.2204288,9.1203738
user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    #g = GeoIP()
    #lat, lng = g.lat_lon(user_ip)
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:6]
    template_name = "shops/index.html"


