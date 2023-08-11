class Persona:
    #Inicio de los constructores
    def __init__(self,nombre="") :
        self.__nombre= nombre
        
    #Nombre
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre=nombre
    
    #Datos
    def datos(self):
        print(f"Nombre completo : {self.get_nombre()}")
        
