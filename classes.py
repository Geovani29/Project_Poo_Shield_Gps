
import urllib
import folium
import requests

class Direction():
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
    
class API(Direction):
    def __init__(self, api_url, key):
        self.api_url = api_url
        self.url = None
        self.key = key
        self.json_data = None
        self.check = None
        
    def get_url(self, pedido):
        self.url = self.api_url + urllib.parse.urlencode({"key":self.key, "from":pedido.inicio, "to":pedido.final})
    
    def get_json(self):
        self.json_data = requests.get(self.url).json()

    def check_code(self):
        self.check = self.json_data["info"]["statuscode"]
        
        if self.check == False:
            self.check = 0
        else:
            self.check = 1
 

class Ruta(API, Direction):
    def __init__(self):
        pass     

    def print(pedido , api):
        if api.check == False:
            trip_duration = api.json_data["route"]["formattedTime"]
            distance = api.json_data["route"]["distance"] * 1.61
            print("=================================================")
            print(f"Información del viaje desde {pedido.inicio.capitalize()} hasta {pedido.final.capitalize()}.")
            print(f"Duración del viaje: {trip_duration}.")
            print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
            print("=================================================")
            print("Indicaciones del viaje")
            
            for each in api.json_data["route"]["legs"][0]["maneuvers"]:
                distance_remaining = distance - each["distance"] * 1.61            
                print(each["narrative"] + " (" + str("{:.2f}".format(distance_remaining)) + " Km faltantes)")
                distance = distance_remaining
                

            
   
class Map(API):
    def __init__(self, api) -> None:
        self.m = folium.Map(location=[api.json_data["route"]["legs"][0]["maneuvers"][0]["startPoint"]["lat"],api.json_data["route"]["legs"][0]["maneuvers"][0]["startPoint"]["lng"]], zoom_start= 13)
        
        pass

    def draw_core_points(self, api):
 
        lista = []
        for each in api.json_data["route"]["legs"][0]["maneuvers"]:
            lista.append([each["narrative"], each["startPoint"]["lng"], each["startPoint"]["lat"]])
        

        for row in lista:
            folium.Marker([row[2], row[1]], popup=row[0]).add_to(self.m)

        
        pass
    
    def draw_lines(self, api):
        lista = []

        for each in api.json_data["route"]["legs"][0]["maneuvers"]:
            lista.append([each["startPoint"]["lat"], each["startPoint"]["lng"]])
            
        folium.PolyLine(lista, color="red", weight=2.5, opacity=1).add_to(self.m)

    def save_map(self):
        
        self.m.save(r"Project_Poo_Shield_Gps\try.html")
