from chilenos import *
from extranjeros import *

class menu():
    def mostrardstos(self):
        
        opcion = 0
        opcion = int(input("Presione 1 si es extranjero y 2 si es chileno"))

        if opcion >=1:
            Extranjero.datos
            pass
        elif opcion ==2:
            Chileno.datos
            pass
        else:
            print("Error")
            
            
menu()