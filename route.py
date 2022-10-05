import osmnx as ox
import networkx as nx


class route:

    def c_danger_zones (self):
        pass

    def generate_route(self):
        
        ox.config(log_console=True, use_cache=True)
        # definir las ubicaciones de inicio y finalización en latlng
        start_latlng = (10.271681232946728, -74.90753173828125)
        end_latlng = (10.371660215460267, -75.0311279296875)
        # ubicación donde desea encontrar su ruta
        place     = 'San Francisco, California, United States'
        # encontrar la ruta más corta según el modo de viaje
        mode      = 'walk'        # 'drive', 'bike', 'walk'
        # encontrar el camino más corto basado en la distancia o el tiempo
        optimizer = 'time'        # 'length','time'
        # crear gráficos desde OSM dentro de los límites de algunos
        # geocodable place(s)
        graph = ox.graph_from_place(place, network_type = mode)
        # encontrar el nodo más cercano a la ubicación de inicio
        orig_node = ox.get_nearest_node(graph, start_latlng)
        # encontrar el nodo más cercano a la ubicación final
        dest_node = ox.get_nearest_node(graph, end_latlng)
        #  encontrar el camino más corto
        shortest_route = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight=optimizer)

        shortest_route_map = ox.plot_route_folium(graph, shortest_route)
        
        
