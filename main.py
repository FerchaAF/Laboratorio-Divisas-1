# from OLDDivisador import CreaDivisador
from divisa import *
from chilenos import *
from persona import *
from menu import *


def validador(opci):
    if opci < 1 or opci > 3:
        return False
    else:
        return True
    

def Main():
    opci = 0
    #LlamadaCalculo = 
    # LlamadaDivisa = Divisa()
    Chilenx = Chileno()
    Extranjerx = Extranjero()
    Individuo = Persona()
    # IniciarMenu = menu()
    
    # LlamadaDivisa
    # Chilenx
    # Extranjerx
    # Individuo
    # IniciarMenu.mostrardstos
    
    while opci != 3:
        opci = int(input("Ingrese 1 para extranjero, 2 para chileno, ingrese 3 para cancelar toda operacion\n"))
        if opci == 1:
            Individuo.set_nombre(input("Favor de ingresar su nombre"))
            Extranjerx.set_nacionalidad(input("Favor de ingresar nacionalidad"))
        if opci == 2:
            Individuo.set_nombre(input("Favor de ingresar su nombre"))
            Chilenx.set_direaccion(input("Favor de ingresar su residencia"))
            Chilenx.set_rut(input("Favor de ingresar su rut"))
            Chilenx.Validacion
        if validador(opci):
            opci = int(input("De verdad desea cancelar la operacion? Ingrese 3 para confirmar\nIngrese 1 para continuar con la operacion de individuo extranjero\nO ingrese 2 para continuar con la operacion de individuo chileno\n"))
    
Main()