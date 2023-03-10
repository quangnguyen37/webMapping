import folium

map = folium.Map(location=[37.774929,-122.419418], zoom_start=9, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[37.297140, -121.833370], popup="This is a marker",tooltip="Rachel is cute", icon=folium.Icon(color="red")))
map.add_child(fg)

map.save("Map1.html")
