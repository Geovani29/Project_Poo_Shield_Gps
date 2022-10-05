import folium 
class map:
    def __init__(self):
        pass

    def draw_map(x):
        
        m = folium.Map(location=[10.916583786068093, -74.77432250976562], zoom_start=12)
        tooltip = x
        folium.Marker([10.916583786068093, -74.77432250976562], 
                    popup='<strong>Location One</strong>',
                    tooltip = tooltip).add_to(m)
        m.save('map.html')
        return 