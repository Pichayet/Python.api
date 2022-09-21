import csv

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = r'C:\Users\gati6\Desktop\Python\Data/world_fires_1_day.csv'
with open(filename) as f:
    all_eq_data = csv.reader(f)
    header_row = next(all_eq_data)
    #all_eq_dicts = all_eq_data['features']

    brightness, lons, lats,hover_texts = [], [], [],[]
    for eq_dict in all_eq_data:
        lon = eq_dict[1]
        lat = eq_dict[0]
        bri = float(eq_dict[2])
        lons.append(lon)
        lats.append(lat)
        brightness.append(bri)
        hover_texts.append(bri)
# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [0.025*bri for bri in brightness],
        'color': brightness,
        'colorscale': 'rainbow',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires_1_day.html')