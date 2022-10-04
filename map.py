import folium

m = folium.Map(location=[42.3601, -71.8589], zoom_start=12)
tooltip = 'Click for more ingo'
folium.Marker([-74.90753173828125, 10.271681232946728], 
              popup='<strong>Location One</strong>',
              tooltip = tooltip).add_to(m)


m.save('map.html')