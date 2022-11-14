
import urllib
import folium
import requests


#Clase que recibe las direcciones
class Direction():
    def __init__(self, inicio: str, final: str)-> None:
        self.inicio = inicio
        self.final = final



#Clase que contiene toda la información de la API de navegación usada
class API(Direction):
    def __init__(self, api_url: str, key: str)-> None:
        self.api_url = api_url
        self.url = None
        self.key = key
        self.json_data = None
        self.check = None
    
    #se obtiene la url
    def get_url(self, pedido: object) -> None:
        self.url = self.api_url + urllib.parse.urlencode({"key":self.key, "from":pedido.inicio, "to":pedido.final})
    
    #se obtiene el json con los datos de navegación
    def get_json(self) -> None:
        self.json_data = requests.get(self.url).json()

    #se verifica si se puede llegar al destino deseado
    def check_code(self) -> None:
        self.check = self.json_data["info"]["statuscode"]
        
        if self.check == False:
            self.check = 0
        else:
            self.check = 1
 


#Clase que nos entrega la ruta que se debe tomar de un punto a otro por medio de indicaciones,
#el tiempo que vamos a demorar y los kilometros de distancia que hay.
class Ruta(API, Direction):
    def __init__(self) -> None:
        pass     

    #metodo que escribe en consola las direcciones que se deben tomar para llegar al destino
    def print(pedido: object , api: object):
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
                

            
#clase que crea el mapa y contiene los metodos para agregar contenido a este
class Map(API):
    #generamos el objeto mapa, se empieza en la locación de inicio del viaje
    def __init__(self, api:object) -> None:
        self.m = folium.Map(location=[api.json_data["route"]["legs"][0]["maneuvers"][0]["startPoint"]["lat"],api.json_data["route"]["legs"][0]["maneuvers"][0]["startPoint"]["lng"]], zoom_start= 13)

    

    #se dibujan los puntos en los que se realiza cada giro
    def draw_core_points(self, api:object) -> None:
 
        lista = []
        for each in api.json_data["route"]["legs"][0]["maneuvers"]:
            lista.append([each["narrative"], each["startPoint"]["lng"], each["startPoint"]["lat"]])
        

        for row in lista:
            folium.Marker([row[2], row[1]], popup=row[0]).add_to(self.m)


    
    #se dibujan las lineas de viaje entre cada uno de los giros
    def draw_lines(self, api:object) -> None:
        lista = []

        for each in api.json_data["route"]["legs"][0]["maneuvers"]:
            lista.append([each["startPoint"]["lat"], each["startPoint"]["lng"]])
            
        folium.PolyLine(lista, color="red", weight=2.5, opacity=1).add_to(self.m)


    #se genera un archivo ".html" y se guarda en carpeta
    def save_map(self)-> None:
        
        self.m.save("Mapita.html")
