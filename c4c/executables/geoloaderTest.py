from pygeocoder import Geocoder

locations = ['New York, NY', '75001 Paris']

def get_geocode(location):
	country = Geocoder.geocode(location).country
	latitude = Geocoder.geocode(location).latitude
	longitude = Geocoder.geocode(location).longitude

	return country, latitude, longitude

print(get_geocode(locations))