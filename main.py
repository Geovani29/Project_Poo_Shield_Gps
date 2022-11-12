from classes import *
from user import User
import json


api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "TPAGE37FU5xR5kvC7LPAeN3snKSUlv0B"

api = API(api_url, key)
ruta = Ruta
user = User()

while True:
    
    pedido = Direction

    user.ask_name()
    
    
    user.presentation()

    pedido.inicio = user.ask_origen()

    if pedido.inicio == 'q':
        break
    
    pedido.final = user.ask_destino()
    
    if pedido.final == 'q':
        break    
    
    
    api.get_url(pedido)
    
    api.get_json()
    map = Map(api)
    
    with open('data.json', 'w') as f:
        json.dump(api.json_data, f)

    #el json se guardó en el atributo api.jason_data
    
    api.check_code()


    ruta.print(pedido, api)

    print("IMPORTANTEEEEEE")
    print(api.json_data["route"]["legs"][0]["maneuvers"][0]["startPoint"])

    map.draw_core_points(api)
    break
    