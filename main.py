from clases import *

api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "TPAGE37FU5xR5kvC7LPAeN3snKSUlv0B"

api = API(api_url, key)
ruta = Ruta

while True:
    
    pedido = direction
        
    pedido.inicio = input("Ingresa el origen: ")

    if pedido.inicio == 'q':
        break
    
    pedido.final = input("Ingresa el destino: ")
    
    if pedido.final == 'q':
        break    
    
    
    api.get_url(pedido)
    
    api.get_json()
    #el json se guardó en el atributo api.jason_data
    
    api.check_code()

    ruta.print(pedido, api)
    