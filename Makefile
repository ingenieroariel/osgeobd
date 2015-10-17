OSMOSIS='osmosis/bin/osmosis'
DB='osmbangladesh'

# Download osm information from the whole country
# updated in the last 24 hours.
bangladesh.pbf:
	wget -O $@ "http://download.geofabrik.de/asia/bangladesh-latest.osm.pbf"

buildings.pbf: bangladesh.pbf
	$(OSMOSIS) --read-pbf-fast file="$<" --tf accept-ways "building=*"  --write-pbf file="$@"

restaurants.pbf: bangladesh.pbf
	$(OSMOSIS) --read-pbf-fast file="$<" --nkv keyValueList="amenity.restaurant,amenity.restaurants" --tf reject-ways --tf reject-relations --write-pbf file="$@"

%.sql: %.pbf
	ogr2ogr -f PGDump $@ $< -lco COLUMN_TYPES=other_tags=hstore --config       OSM_CONFIG_FILE conf/$(basename $@).ini

%.postgis: %.sql
	psql -f $< $(DB)
	psql -f conf/$(basename $@)_alter.sql $(DB)
	psql -f conf/clean.sql -q $(DB)
