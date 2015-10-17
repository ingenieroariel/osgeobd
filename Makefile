OSMOSIS='osmosis/bin/osmosis'

# Download osm information from the whole country
# updated in the last 24 hours.
bangladesh.pbf:
	wget -O $@ "http://download.geofabrik.de/asia/bangladesh-latest.osm.pbf"


restaurants.pbf: bangladesh.pbf
	$(OSMOSIS) --read-pbf-fast file="$<" --nkv keyValueList="amenity.restaurant,amenity.restaurants" --tf reject-ways --tf reject-relations --write-pbf file="$@"
