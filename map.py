import folium 
class map:
    def __init__(self):
        pass

    def draw_map(x,lat,lon):
        
        m = folium.Map(location=[lat, lon], zoom_start=12)
        tooltip = x
        folium.Marker([lat, lon], 
                    popup='<strong>Location One</strong>',
                    tooltip = tooltip).add_to(m)
        m.save('map.html')
        return 