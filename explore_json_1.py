import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

# the json.load() function converts the data into workable data
eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

print(eq_data["features"][0]["properties"]["mag"])