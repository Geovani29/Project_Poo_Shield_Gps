import urllib

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
            #fuel_used = api.json_data["route"]["fuelUsed"] * 3.79
            print("=================================================")
            print(f"Información del viaje desde {pedido.inicio.capitalize()} hasta {pedido.final.capitalize()}.")
            print(f"Duración del viaje: {trip_duration}.")
            print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
            #print("Combustible usado: " + str("{:.2f}".format(fuel_used) + " L"))
            print("=================================================")
            print("Indicaciones del viaje")

            for each in api.json_data["route"]["legs"][0]["maneuvers"]:
                distance_remaining = distance - each["distance"] * 1.61            
                print(each["narrative"] + " (" + str("{:.2f}".format(distance_remaining)) + " Km faltantes)")
                distance = distance_remaining
            
   
