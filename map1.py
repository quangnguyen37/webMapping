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
    
map = folium.Map(location=[37.774929,-122.419418], zoom_start=9, tiles = 'Stamen Toner')

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elevation):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup= folium.Popup(iframe),tooltip="Rachel is cute", radius= 6, fill =True, 
                                     fill_opacity = 1 , fillColor=color_elevation(el), color = 'grey'))


fg.add_child(folium.GeoJson(data = open('world.json', 'r', encoding= 'utf-8-sig').read(), 
                            style_function= lambda x: {'fillColor':'yellow' if x['properties'] ['POP2005'] < 1000000
                                                       else 'green' if 1000000 <= x['properties']['POP2005'] < 5000000
                                                       else 'blue' if 5000000 <= x['properties']['POP2005'] < 10000000
                                                       else 'purple' if 10000000 <= x['properties']['POP2005'] <50000000
                                                       else 'black'if 50000000 <= x['properties']['POP2005'] <100000000
                                                       else 'red', 
                                                       'lineColor': '#FFFFFF', 
                                                       'weight': '0.2'}))


map.add_child(fg)

map.save("Map1.html")
