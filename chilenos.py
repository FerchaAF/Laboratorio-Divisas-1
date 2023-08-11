from persona import *
from itertools import cycle

class Chileno(Persona):
    #Inicio de los constructores
    def __init__(self, nombre="", monto=0.0, dnombre="", rut=0, direccion=""):
        # super().__init__(nombre, monto, dnombre)
        self.__rut = rut
        self.direccion= direccion
    #Getter y Setter (Rut y direccion)"
    def get_direccion(self):
        return self.__direccion
    def set_direaccion(self,direccion):
        self.__direccion=direccion

    def get_rut(self):
        return self.__rut
    def set_rut(self,rut):
        self.__rut=rut

    #Validacion del rut
    def Validacion(rut):
        reversed_digits =map(int,reversed(str(rut)))
        factors=cycle(range(2, 8))
        s=sum(d*f for d, f in zip(reversed_digits,factors))
        return (-s) % 11
    #Datos
    def datos(self):
        super().datos()
        print(f"Rut : {self.get_rut()}")
        print(f"Direccion : {self.get_direccion()}")
