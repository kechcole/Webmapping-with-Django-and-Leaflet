from django.contrib.gis.db import models    # Models for gis

# Create your models here.

# Create first model 
class City(models.Model):
    # City name attribute 
    name = models.CharField(max_length=200)

    # Place coordinates
    location = models.PointField(srid=4326) 

    # Return incident name in the admin/backend section 
    def __unicode__(self):
        return self.name
    
    # Curb plural model naming 
    class Meta:
        verbose_name_plural = "Cities"


#  Second model for world countries 
class WorldCountries(models.Model):
    fips = models.CharField(max_length=2, null=True)
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


# Third model containing kenyan cities with population data in geojson
# Model generated automatically 
class KenyanCities(models.Model):
    city = models.CharField(max_length=200)
    pop = models.IntegerField()
    geom = models.MultiPointField(srid=4326)

    # Return country name
    def __str__(self):
        return self.city
    
    # Curb plural model naming 
    class Meta:
        verbose_name_plural = "KenyanCitiess"



