from django.shortcuts import render

# Import classed base template view
from django.views.generic import TemplateView


      # SERIALIZATION 
from .models import KenyanCities, WorldCountries    # Import data models from views
from django.core.serializers import serialize    # Serializer 

from django.http import HttpResponse    # Http response that return information / data


# Create your views here.
# class based view Homepage 
class HomePageView(TemplateView):
    template_name = 'index.html'


# function based views that serialize datasets.
def world_dataset(request):
	# Serialize worldCountries objects into geojson and assign name countries
	countries = serialize('geojson', WorldCountries.objects.all())
	return HttpResponse(countries, content_type='json')   # Return json format

def kecities_datasets(request):
	# Serialize kenyanCities model into geojson, 
	ke_cities = serialize('geojson', KenyanCities.objects.all())
	return HttpResponse(ke_cities, content_type='json')  # Return json format