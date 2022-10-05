import folium 
class map:
    def __init__(self):
        pass

    def draw_map(x1,lat1,lon1,x2,lat2,lon2):
        
        m = folium.Map(location=[lat1, lon1], zoom_start=12)
        tooltip1 = x1
        tooltip2 = x2
        folium.Marker([lat1, lon1], 
                    popup='<strong>Location One</strong>',
                    tooltip = tooltip1).add_to(m)
        folium.Marker([lat2, lon2], 
                    popup='<strong>Location One</strong>',
                    tooltip = tooltip2).add_to(m)
        m.save('map.html')
        return 