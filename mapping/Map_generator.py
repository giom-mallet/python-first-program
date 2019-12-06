import folium
import pandas

#Create a Map centered on Reyvialle

#supermap = folium.Map(location=[45.717461, 2.82085], zoom_start=20)
#supermap.save("Reyvialle.html")
stamenmap = folium.Map(location=[45.717461, 2.82085], zoom_start=5, tiles="Stamen Terrain")


volc_data = pandas.read_csv("Volcanoes.txt")
lat = list(volc_data["LAT"])
lon = list(volc_data["LON"])
name = list(volc_data["NAME"])
elev = list(volc_data["ELEV"])

volcano_group = folium.FeatureGroup(name="Volcanoes")
country_group = folium.FeatureGroup(name="Countries")


def pop_colors(feature):
    pop = feature["properties"]["POP2005"]
    if pop < 10000000 :
        return {'fillColor' : 'green'}
    elif pop > 100000000  :
        return {'fillColor' : 'red'}
    else :
        return {'fillColor' : 'orange'}

def el_colors(elevation):
    elev = float(elevation)
    if elev < 1000.0:
        return 'green'
    elif elev > 3000.0:
        return 'orange'
    else:
        return 'red'


country_group.add_child(folium.GeoJson(data=open('world.json','r',encoding = 'utf-8-sig').read(),
style_function=pop_colors
))

for lati, longi, name, elev in zip(lat, lon, name , elev):
    html = "<h4>{}</h4><br/>Elevation: {} m".format(name, elev)
    volcano_group.add_child(folium.CircleMarker(location=[lati, longi],
    popup=html,
    radius=10,
    color="grey",
    fill_color=el_colors(elev),
    fill = el_colors(elev), 
    fill_transparency = 0.9)
    )

stamenmap.add_child(country_group)
stamenmap.add_child(volcano_group)
stamenmap.save("Reyvialle_terrain.html")