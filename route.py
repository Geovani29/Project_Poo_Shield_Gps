import osmnx as ox
import networkx as nx


class route:

    def c_danger_zones (self):
        pass

    def generate_route(self):
        
        ox.config(log_console=True, use_cache=True)
        # define the start and end locations in latlng
        start_latlng = (10.271681232946728, -74.90753173828125)
        end_latlng = (10.371660215460267, -75.0311279296875)
        # location where you want to find your route
        place     = 'San Francisco, California, United States'
        # find shortest route based on the mode of travel
        mode      = 'walk'        # 'drive', 'bike', 'walk'
        # find shortest path based on distance or time
        optimizer = 'time'        # 'length','time'
        # create graph from OSM within the boundaries of some 
        # geocodable place(s)
        graph = ox.graph_from_place(place, network_type = mode)
        # find the nearest node to the start location
        orig_node = ox.get_nearest_node(graph, start_latlng)
        # find the nearest node to the end location
        dest_node = ox.get_nearest_node(graph, end_latlng)
        #  find the shortest path
        shortest_route = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight=optimizer)

        shortest_route_map = ox.plot_route_folium(graph, shortest_route)
        
        shortest_route_map = [10.271681232946728, -74.90753173828125, 10.371660215460267, -75.0311279296875]
        
        
        
