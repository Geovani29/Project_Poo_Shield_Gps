import folium 
class map:
    def __init__(self):
        pass

<<<<<<< HEAD
    def draw_map(x):
        
        m = folium.Map(location=[10.916583786068093, -74.77432250976562], zoom_start=12)
        tooltip = x
        folium.Marker([10.916583786068093, -74.77432250976562], 
                    popup='<strong>Location One</strong>',
                    tooltip = tooltip).add_to(m)
=======
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
>>>>>>> 40d4f09f38e226d9b3dd65363415eb0d094a2180
        m.save('map.html')
        return 