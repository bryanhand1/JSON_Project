import json

# Need to open each file and create new readable files


infile2 = open("US_fires_9_14.json", "r")
outfile2 = open("read_files_2.json", "w")

fire_data2 = json.load(infile2)

json.dump(fire_data2, outfile2, indent=4)

# Now to view data
# print(type(fire_data1))
# make a list of fires for each file
# we only want fires with brightness over 450
# first make empty list of fires


bright2 = []
lat2 = []
lon2 = []

for i in fire_data2:
    if i["brightness"] >= 450:
        brightness = i["brightness"]
        lat = i["latitude"]
        lon = i["longitude"]
        bright2.append(brightness)
        lat2.append(lat)
        lon2.append(lon)

# print(bright2)

# Now to set up the graphs
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data2 = [
    {
        "type": "scattergeo",
        "lon": lon2,
        "lat": lat2,
        "marker": {
            "color": bright2,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout2 = Layout(title="US Fires 9/14")

fig = {"data": data2, "layout": my_layout2}

offline.plot(fig, filename="fires_9_14.html")
