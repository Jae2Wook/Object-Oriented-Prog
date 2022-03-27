# %%
import requests

# Source of data: http://open-notify.org/

url = 'http://api.open-notify.org/iss-now.json'

req = requests.get(url)
print(type(req.text)) # "": reading from server
print(type(req.json())) # json: function, '': reading from dictionary
print()
print(req.text)
print(req.json())
print()

data = req.json()
print(data)
print()
print(data["iss_position"]["latitude"])

url = 'http://api.open-notify.org/astros.json'

req = requests.get(url)
data = req.json()
for astros in data["people"]:
    print(astros["name"])
print()
print()

# %%
import requests
import pandas


# Source of data: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson'

req = requests.get(url)
data = req.json()
#print(data)
# magnitude and place for everyearthquack
for i in data["features"]:
    print("mag: ", i["properties"]["mag"], "palce: ", i["properties"]["place"])
print()

# %%

# or
earthquake_list = []
for earth in data["features"]:
    mag = earth["properties"]["mag"]
    place = earth["properties"]["place"]
    #print(mag, place)
    earthquake_list.append(earth["properties"])
print()

# df = pandas.Dataframe(liat of dictionaries where each dictionary is an earthquack)
df = pandas.DataFrame(earthquake_list)
print(df)
print(df.mag.mean())
#df = df.mag.sort_values(ascending = False)
df1 = df.sort_values(by = "mag", ascending = False)
print(df)
print(df1[["mag", "place"]])

import matplotlib.pyplot as plt
df1.plot(kind = "bar", x = "place", y = "mag")
plt.show()