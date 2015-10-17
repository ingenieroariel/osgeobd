from django.contrib.gis import admin

from osm.models import Restaurant, Building

class RestaurantAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'other_tags']
    search_by = ['name',]
    order_by = ['name',]

class BuildingAdmin(admin.OSMGeoAdmin):
    list_display = ['osm_id', 'amenity']
    list_filter = ['amenity',]
    search_by = ['name',]
    order_by = ['amenity',]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Building, BuildingAdmin)

