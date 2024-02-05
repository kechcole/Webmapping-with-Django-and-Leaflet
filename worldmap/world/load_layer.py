# MAPP THE DATA AND THE MODEL THEN LOAD DATA INTO THE DATABASE.

# import modules and models
import os 
from django.contrib.gis.utils import LayerMapping
from .models import WorldCountries


# Auto-generated `LayerMapping` dictionary for WorldCountries model
# Each key in the world_mapping dictionary corresponds to a field in the WorldBorders
# model, and the value is the name of the shapefile field that data will be loaded from.
worldcountries_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}


# Locate the datasource path in avariable 
world_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), '/datasource/TM_WORLD_BORDERS-0.3.shp'))
world_shp_fullpath = 'D:/WHole Django/Worldmap project/worldmap/data/TM_WORLD_BORDERS-0.3.shp'

# Load the data into the database 
def run(verbose=True):
    # Actual mapping, coz map already transformed give a value of false, else would give srid number
    lm = LayerMapping(WorldCountries, world_shp_fullpath,  # layers to be mapped 
                      worldcountries_mapping,   # Dictionary containing the data varaiables
                      transform = False,        # Do not transform the data it's already in WGS84
                      encoding = 'iso-8859-1'    # encoding, ensures that string values are read and saved correctly from their original encoding system
                      ) 
    
    # Save the data and match all the fields 
    lm.save(strict=True, verbose=verbose)