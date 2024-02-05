# AFTER CREATING MODEL REGISTER HERE 

from django.contrib import admin
from .models import City, WorldCountries, KenyanCities  # Import model
from leaflet.admin import LeafletGeoAdmin  # Import leaflet

# Register your models here.
# Create an admin for the model
class CityAdmin(LeafletGeoAdmin):
    # WHAT TO display in the admin, fields must correspond with model object
    list_display = ['name', 'location']


# Register shapefile model 
class WorldCountriesAdmin(LeafletGeoAdmin):
    list_display = ['name', 'region', 'pop2005', 'subregion']


# Register geojson generated model
class KenyanCitiesAdmin(LeafletGeoAdmin):
    list_display = ['city', 'pop']


# Register models into the admin
admin.site.register(City, CityAdmin)
admin.site.register(WorldCountries, WorldCountriesAdmin)
admin.site.register(KenyanCities, KenyanCitiesAdmin)



