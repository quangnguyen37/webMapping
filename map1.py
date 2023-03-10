import folium
import pandas

vol_coord = pandas.read_csv("Volcanoes.txt")

lat = list(vol_coord["LAT"])
lon = list(vol_coord["LON"])
elevation = list(vol_coord["ELEV"])

map = folium.Map(location=[37.774929,-122.419418], zoom_start=9, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elevation):
    fg.add_child(folium.Marker(location=[lt, ln], popup= str(el) + " Meters",tooltip="Rachel is cute", icon=folium.Icon(color="red")))



map.add_child(fg)

map.save("Map1.html")
