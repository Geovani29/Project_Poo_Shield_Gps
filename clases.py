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
 

    