from persona import *
from chilenos import *
from extranjeros import *

class Divisa():
    def __init__(self, monto=0.0, dnombre="") :
        self.__monto= monto
        self.__dnombre= dnombre
        
    #Monto en CLP 
    def get_monto(self):
        return self.__monto
    def set_monto(self,monto):
        self.__monto=monto
    #Nombre de la divisa
    def get_dnombre(self):
        return self.__dnombre
    def set_dnombre(self,dnombre):
        self.__dnombre=dnombre
    