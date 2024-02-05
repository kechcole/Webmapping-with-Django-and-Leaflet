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
Database connection is established with appropriate credetials and then enable gdal in INSTALLED APP variable by including the contrib.gis module. 

## 3. Geographic Data Modelling. 




