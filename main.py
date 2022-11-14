from classes import *
from user import User
import json

#se toman la url y la key para que la API funcione
api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "TPAGE37FU5xR5kvC7LPAeN3snKSUlv0B"

#se crean algunos objetos
api = API(api_url, key)
ruta = Ruta
user = User()

#el while permite que el codigo se repita si el usuario comete algun error
while True:
    
    #se crea el objeto pedido
    pedido = Direction

    #se realiza una presentación al usuario
    user.ask_name()
    
    user.presentation()

    pedido.inicio = user.ask_origen()

    #si el usuario decide salir escribiendo "salir" en consola al preguntarle su origen o destino, el programa acabará
    if pedido.inicio == 'Salir':
        break
    
    pedido.final = user.ask_destino()
    
    if pedido.final == 'Salir':
        break    
    
    #se obtiene la url 
    api.get_url(pedido)
    
    #se genera el json con los datos de navegación, el json se guardó en el atributo api.jason_data
    api.get_json()

    #se crea el mapa con los datos de la api
    map = Map(api)
    
    #se guarda el json como archivo (esto es para debuggin)
    with open('data.json', 'w') as f:
        json.dump(api.json_data, f)

    #se checa que sí se puede realizar el viaje pedido
    api.check_code()

    #se imprimen las intrucciones del viaje
    ruta.print(pedido, api)

    #se dibujan en el mapa los puntos de giro, las lineas entre estros y al final se guarda como .html en carpeta
    map.draw_core_points(api)

    map.draw_lines(api)

    map.save_map()
    
    break
    