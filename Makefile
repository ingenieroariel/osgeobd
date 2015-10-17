# Download osm information from the whole country
# updated in the last 24 hours.
bangladesh.pbf:
	wget -O $@ "http://download.geofabrik.de/asia/bangladesh-latest.osm.pbf"
