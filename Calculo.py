from divisa import *

class calculo():
    n = 0
    def __init__(self, monto=0.0, dnombre=""):
        super().__init__(monto, dnombre)
        self.__dnombre= dnombre
        self.__monto = monto
        
    def get_monto(self):
        return self.__monto
    def set_monto(self,monto):
        self.__monto=monto
    #Nombre de la divisa
    def get_dnombre(self):
        return self.__dnombre
    def set_dnombre(self,dnombre):
        self.__dnombre=dnombre
        
    def conversion(self):
        dnombre = self.__dnombre
        monto = self.__monto
        if dnombre.lower == "yenes":
            f_monto = monto*()
        elif dnombre.lower == "dolares":
            f_monto = monto*()
        elif dnombre.lower == "soles":
            f_monto = monto*()
        elif dnombre.lower == "euros":
            f_monto = monto*()
        elif dnombre.lower == "libras":
            f_monto = monto*()
        return f_monto

    def transcacciones(n):
        n+=1
        
    def datos(self):
        super().datos()
        print(f"Nombre de la Divisa: {self.get_dnombre()}")
        print(f"Monto : {self.conversion()}, {self.__monto()}" )