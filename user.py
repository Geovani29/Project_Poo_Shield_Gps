class User:

    def __init__(self):

        self.name = None


        pass

    def ask_name(self):
        print("=================================================")
        self.name = input("¿cual es su nombre? Querido usuario: ")
        print("=================================================")
        

    def presentation(self):
        print("===============================================================================")
        print("Hola "+ self.name +" yo soy SHIELD_GPS tu GPS de confianza ¿A donde quieres ir?")
        print("===============================================================================")
        
        return 

    def ask_origen(self):

        return input("Ingresa el origen: ")

    def ask_destino(self):

        return input("Ingresa el destino: ")
