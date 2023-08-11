from persona import *
class Extranjero(Persona):
    #Inicio de los constructores
    def __init__(self,nombre="", monto=0.0, dnombre="", nacionalidad=""):
        # super().__init__(nombre, monto, dnombre)
        self.__nacionalidad = nacionalidad
    #Nacionalidad
    def get_nacionalidad(self):
        return self.__nacionalidad
    def set_nacionalidad(self,nacionalidad):
        self.__nacionalidad=nacionalidad
    #Datos
    def datos(self):
        super().datos()
        print(f"Nacionalidad : {self.get_nacionalidad()}")
