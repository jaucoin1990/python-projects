import folium
import pandas as pd


map = folium.Map(location=[44.044359, -123.073114], zoom_start=5)


def color_producer(el):
    if el < 1000.0:
        return "lightblue"
    elif el < 2000.0:
        return "blue"
    elif el < 3000.0:
        return "darkblue"
    elif el < 4000.0:
        return "red"
    else:
        return "darkred"


def map_fun(file, lat, lon, elev):

    data = pd.read_csv(file)
    lat = list(data[lat])
    lon = list(data[lon])
    elev = list(data[elev])

    fg = folium.FeatureGroup(name="My Map of Volcanoes")

    for lt, ln, el in zip(lat, lon, elev):
        fg.add_child(folium.Marker(location=(lt, ln), popup=str(el) + "m", icon=folium.Icon(color=color_producer(el))))
        
    map.add_child(fg)
    map.save("map1.html")



map_fun("Volcanoes.txt", "LAT", "LON", "ELEV")



