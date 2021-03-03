import json

# Need to open each file and create new readable files
infile1 = open("US_fires_9_1.json", "r")
outfile1 = open("readable_files_1.json", "w")

fire_data1 = json.load(infile1)

json.dump(fire_data1, outfile1, indent=4)


# Now to view data
# print(type(fire_data1))
# make a list of fires for each file
# we only want fires with brightness over 450
# first make empty list of fires
bright1 = []
lat1 = []
lon1 = []

for i in fire_data1:
    if i["brightness"] >= 450:
        brightness = i["brightness"]
        lat = i["latitude"]
        lon = i["longitude"]
        bright1.append(brightness)
        lat1.append(lat)
        lon1.append(lon)

# print(bright1)


# Now to set up the graphs
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data1 = [
    {
        "type": "scattergeo",
        "lon": lon1,
        "lat": lat1,
        "marker": {
            "color": bright1,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout1 = Layout(title="US Fires 9/1")

fig = {"data": data1, "layout": my_layout1}

offline.plot(fig, filename="fires_9_1.html")
