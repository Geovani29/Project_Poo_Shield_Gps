class User:

    def __init__(self):

        self.name = None


        pass
    #Pide el nombre al usario
    def ask_name(self):
        print("=================================================")
        self.name = input("¿cual es su nombre? Querido usuario: ")
        print("=================================================")
        
    #Se presenta con el usuario
    def presentation(self):
        print("===============================================================================")
        print("Hola "+ self.name +" yo soy SHIELD_GPS tu GPS de confianza ¿A donde quieres ir?")
        print("===============================================================================")
        
        return 
    #Pide el lugar de origen de donde se quiere viajar (Puede ser direccion exacta, ciudad, pais, etc)
    def ask_origen(self):

        return input("Ingresa el origen: ")
    #Pide el lugar de destino a donde se quiere viajar (Puede ser direccion exacta, ciudad, pais, etc)
    def ask_destino(self):

        return input("Ingresa el destino: ")
