# from geopy.geocoders import Nominatim

# geolocator = Nominatim()
# # result = geolocator.geocode("175 5th Avenue NYC")
# result = geolocator.geocode("London SW1A 1AA, UK")
# resultAddress = result.address
# fields = resultAddress.split(",")
# country = fields[(len(fields) - 1)]
# print(country)
# result2 = geolocator.reverse(','.join(fields[1:3]), language='en')

# {'place_id': '132198335', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', 'osm_type': 'way', 'osm_id': '264768896', 'boundingbox': ['40.7407597', '40.7413004', '-73.9898715', '-73.9895014'], 'lat': '40.7410861', 'lon': '-73.9896298241625', 'display_name': 'Flatiron Building, 175, 5th Avenue, Flatiron Building, Manhattan Community Board 5, New York County, NYC, New York, 10010, United States of America', 'class': 'tourism', 'type': 'attraction', 'importance': 0.79300331552197, 'icon': 'https://nominatim.openstreetmap.org/images/mapicons/poi_point_of_interest.p.20.png'}

# print(result.address)
# print(result.raw['display_name'])
# print(result.country)
# print(result.coordinates)
# print(result.latitude)
# print(result.longitude)

import time
from pygeocoder import Geocoder
#import pandas as pd 
#import numpy as np 

locals = ["London SW1A 1AA, UK", "qwertasdf", "Tucson, AZ", "Washington, DC"]

for local in locals:
# result = Geocoder.geocode("1600 Pennsylvania Ave NW, Washington, DC 20006")
# result = Geocoder.geocode("Tucson, AZ")
# result = Geocoder.geocode("London SW1A 1AA, UK")
    try:
    	result = Geocoder.geocode(local)
    	print(result.country)
    	print(result.coordinates)
    	print(result.latitude)
    	print(result.longitude)
    except:
    	continue
    print("continues on")
    time.sleep(0.25)

# # Create a dictionary of raw data
# data = {'Site 1': '31.336968, -109.560959',
#         'Site 2': '31.347745, -108.229963',
#         'Site 3': '32.277621, -107.734724',
#         'Site 4': '31.655494, -106.420484',
#         'Site 5': '30.295053, -104.014528'}

