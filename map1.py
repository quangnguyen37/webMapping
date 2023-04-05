import folium
import pandas

vol_coord = pandas.read_csv("volcano.csv")

lat = list(vol_coord["LAT"])
lon = list(vol_coord["LONG"])
volcanoName = list(vol_coord["VOLCANO"])
lastErup = list(vol_coord["ERUPTED"])
elevation = list(vol_coord["ELEV_M"])

html = """<h5>Volcano information:</h5>
<body>Height: %s meters</body>
<br>
<body>Last Erupted: %s </body>
"""

def color_elevation(elevation):
    if elevation < 1000:
        return 'lightgreen'
    if elevation < 3000:
        return 'orange'
    else:
        return 'red'
    
map = folium.Map(location=[37.774929,-122.419418], zoom_start=9, tiles = 'Stamen Toner')

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name, date in zip(lat, lon, elevation, volcanoName,lastErup):
    iframe = folium.IFrame(html=html % (str(el), str(date)), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup= folium.Popup(iframe),tooltip= name , radius= 6, fill =True, 
                                     fill_opacity = 1 , fillColor=color_elevation(el), color = 'grey'))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding= 'utf-8-sig').read(), 
                            style_function= lambda x: {'fillColor':'yellow' if x['properties'] ['POP2005'] < 1000000
                                                       else 'green' if 1000000 <= x['properties']['POP2005'] < 5000000
                                                       else 'blue' if 5000000 <= x['properties']['POP2005'] < 10000000
                                                       else 'purple' if 10000000 <= x['properties']['POP2005'] <50000000
                                                       else 'black'if 50000000 <= x['properties']['POP2005'] <100000000
                                                       else 'red', 
                                                       'lineColor': '#FFFFFF', 
                                                       'weight': '0.2'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())


map.save("Map1.html")
