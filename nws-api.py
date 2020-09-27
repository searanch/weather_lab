import requests
import json

#Use get to make request for NWS api.

# Store url in variable
url = "https://api.weather.gov/gridpoints/MPX/108,69/forecast"

#response = requests.get(url)

#print(requests.get(url).json())

# Pretty Print the output of the JSON
response = requests.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))

# It is possible to grab a specific value 
# from within the JSON object
print(response["detailedForecast"])
