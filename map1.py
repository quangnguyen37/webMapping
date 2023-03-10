import folium
import pandas

vol_coord = pandas.read_csv("Volcanoes.txt")

lat = list(vol_coord["LAT"])
lon = list(vol_coord["LON"])
elevation = list(vol_coord["ELEV"])

html = """<h5>Volcano information:</h5>
<h5>Height: %s meters</h5>
"""

def color_elevation(elevation):
    if elevation < 1000:
        return 'lightgreen'
    if elevation < 3000:
        return 'orange'
    else:
        return 'red'
    
map = folium.Map(location=[37.774929,-122.419418], zoom_start=9, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elevation):
    iframe = folium.IFrame(html=html % str(el), width=150, height=75)
    fg.add_child(folium.Marker(location=[lt, ln], popup= folium.Popup(iframe),tooltip="Rachel is cute", icon=folium.Icon(color=color_elevation(el))))





map.add_child(fg)

map.save("Map1.html")
