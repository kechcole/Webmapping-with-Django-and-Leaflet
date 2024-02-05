# MAPP THE DATA AND THE MODEL THEN LOAD DATA INTO THE DATABASE.

# import modules and models
import os 
from django.contrib.gis.utils import LayerMapping
from .models import KenyanCities

# Auto-generated `LayerMapping` dictionary for KenyanCities model
kenyancities_mapping = {
    'city': 'city',
    'pop': 'pop',
    'geom': 'MULTIPOINT',
}

# Locate the datasource path in avariable 
world_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), '/data/ketowns_pop_geojson/citypopKenya.geojson'))
ke_citiesgeojson_fullpath = 'D:/WHole Django/Worldmap project/worldmap/data/ketowns_pop_geojson/citypopKenya.geojson'

# Load the data into the database 
def run(verbose=True):
    # Actual mapping, coz map already transformed give a value of false, else would give srid number
    lm = LayerMapping(KenyanCities, ke_citiesgeojson_fullpath,  # layers to be mapped 
                      kenyancities_mapping,   # Dictionary containing the data varaiables
                      transform = False,        # Do not transform the data it's already in WGS84
                      encoding = 'iso-8859-1'    # encoding, ensures that string values are read and saved correctly from their original encoding system
                      ) 
    
    # Save the data and match all the fields 
    lm.save(strict=True, verbose=verbose)