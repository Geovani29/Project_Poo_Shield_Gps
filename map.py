import folium

m = folium.Map(location=[42.3601, -71.8589], zoom_start=12)
tooltip = 'Click for more ingo'
folium.Marker([42.363600, -71.099500], 
              popup='<strong>Location One</strong>',
              tooltip = tooltip).add_to(m)


m.save('map.html')