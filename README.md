# Webmapping-with-Django-and-Leaflet
Demographic Web Map Application.


## 1. Introduction.
A simple world demographic map that incoorperates geodjango-geojson, GDAL, PostgreSQL(Post GIS Extension) and django-leaflet making the it extremely lightweight. 

Basic features include :

* Django model fields for OGC geometries.
* Extensions to Django’s ORM for the querying and manipulation of spatial data.
* High-level Python interfaces for GIS geometry operations and data formats.
* Editing of geometry fields inside the admin.

## 2. Folder Setup. 

### Create Spatial Database.
A spatial database was created to store data, in this case a PostgreSQL RDMS with Post GIS extension enabled. 
```sql
CREATE TABLE worldmap;
```

### Create GeoDjango Project. 
Installing virtual enviroment with these dependancies : Django, Django-leaflet , gdal wheel, psycopg2 from the command line. 

### Configure settings file. 
Database connection is established with appropriate credetials and then enable gdal and leaflet in INSTALLED APP variable by including the contrib.gis module. 

## 3. Geographic Data Modelling. 
The shapefile containing countries geometries with their corresponding population data must be modelled in a PostreSQL database and be displayed in a Django admin model.

To display data in the layer, it must be added to the database from where it can be read by the Django. Before uploading to postgres we need to create a model and map the vector data. Create a file called load.py inside the world application and use code that maps the vector data fields into our model. The code will be generated automatically by a LayerMapping import utility from the OGR library. 
Generate a model definition and LayerMapping dictionary automatically by passing the data source, model name, SRID and other options. 

Quit the python shell and run:
```console
py manage.py ogrinspect data/TM_WORLD_BORDERS-0.3.shp WorldCountries --srid=4326 --mapping --multi
```
The command produces an output, copy the model into models.py file, write a function to display country name(name attribute) and add Meta class to curb model plural naming. 
```python
# model for world countries 
class WorldCountries(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.BigIntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    
    # Return country name
    def __str__(self):
        return self.name
    
    # Curb plural model naming 
    class Meta:
        verbose_name_plural = "WorldCountries"
```
 
 Import and register the model in the admin.py file. 
 ```python
# Model registration

from django.contrib import admin
from .models import City, WorldCountries  # Import model
from leaflet.admin import LeafletGeoAdmin  # Import leaflet

# Create an admin for the model
class CityAdmin(LeafletGeoAdmin):
    # WHAT TO display in the admin, fields must correspond with model object
    list_display = ['name', 'location']

# Register shapefile model 
class WorldCountriesAdmin(LeafletGeoAdmin):
    list_display = ['name', 'region', 'pop2005', 'region']

# Register models into the admin
admin.site.register(City, CityAdmin)
admin.site.register(WorldCountries, WorldCountriesAdmin)
 ```

## 4. Layer Mapping. 
 A file loadlayer.py was created inside the world application, used to map the model and loading data into the database. It contained this code ;
 ```python
 # import modules and models
import os 
from django.contrib.gis.utils import LayerMapping
from .models import WorldCountries

# Auto-generated `LayerMapping` dictionary for WorldCountries model
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
world_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), '/datasource/ TM_WORLD_BORDERS-0.3.shp'))
world_shp_fullpath = 'D:/WHole Django/Worldmap project/worldmap/data/TM_WORLD_BORDERS-0.3.shp'

# Load the data into the database 
def run(verbose=True):
    # Actual mapping, coz map already transformed give a value of false, else would give srid number
    lm = LayerMapping(WorldCountries, world_shp_fullpath,  
                        # layers to be mapped 
                      worldcountries_mapping,   # Dictionary containing the data varaiables
                      transform = False,        # Do not transform the data
                      encoding = 'iso-8859-1'    #encoding
                      ) 
    
    # Save the data and match all the fields 
    lm.save(strict=True, verbose=verbose)
 ``` 
 To effect the above changes in the database, we need to migrate the new model into the database from the python shell. 
 ```console
 py manage.py makemigrations    
py manage.py migrate   
 ```





