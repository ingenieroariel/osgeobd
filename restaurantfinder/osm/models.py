from __future__ import unicode_literals

from django.contrib.gis.db import models


class Building(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
#    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'buildings'


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
#    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'restaurants'

def fixrestaurants():
    for restaurant in Restaurant.objects.all():
        buildings = Building.objects.filter(geom__intersects=restaurant.geom)
        if buildings.count() == 1:
            print buildings[0].osm_way_id, restaurant.id
            restaurant.is_in = buildings[0].osm_way_id
            restaurant.save()
