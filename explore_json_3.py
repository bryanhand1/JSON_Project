import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

# the json.load() function converts the data into workable data
eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

# print(eq_data["features"][0]["properties"]["mag"])

list_of_eqs = eq_data["features"]

mags = []
lons = []
lats = []
hover_texts = []

for i in range(len(list_of_eqs)):
    mags.append(list_of_eqs[i]["properties"]["mag"])
    lons.append(list_of_eqs[i]["geometry"]["coordinates"][0])
    lats.append(list_of_eqs[i]["geometry"]["coordinates"][1])
    hover_texts.append(list_of_eqs[i]["properties"]["place"])
"""
print(mags[:10])
print(lons[:10])
print(lats[:10])
"""

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
