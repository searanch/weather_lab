import requests
import json

# Impoted Python Package for a easier way to access api

from noaa_sdk import noaa

#Search fpr current weather in my zip code
n = noaa.NOAA()
res = n.get_forecasts('55407', 'US', True)


# create json object
json_object = json.dumps(res, indent = 4,sort_keys=True)   
print(json_object)


