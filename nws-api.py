import requests
import json

# Impoted Python Package for a easier way to access api

from noaa_sdk import noaa

# Search fpr current weather in my zip code
n = noaa.NOAA()
res = n.get_forecasts('55407', 'US', True)
for i in res:
    print(i)

print(type(i))


json_object = json.dumps(i, indent = 4)   
print(json_object)  

