from classes import *
from user import User
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
    #el json se guardó en el atributo api.jason_data
    
    api.check_code()


    ruta.print(pedido, api)
    break
    