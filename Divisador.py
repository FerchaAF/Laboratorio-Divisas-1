class CreaDivisador():
    def __init__(self, Euro, Dolar, Sol, PMexicano, Yen):
        self.__DivisaEur = Euro 
        self.__DivisaDol = Dolar
        self.__DivisaSol = Sol
        self.__DivisaMex = PMexicano
        self.__DivisaYen = Yen
    
    ## SETTER

    def setDivisaEur(self, Euro):
        self.__DivisaEur = Euro

    def setDivisaDol(self, Dolar):
        self.__DivisaDol = Dolar

    def setDivisaSol(self, Sol):
        self.__DivisaSol = Sol

    def setDivisaMex(self, PMexicano):
        self.__DivisaMex = PMexicano

    def setDivisaYen(self, Yen):
        self.__DivisaYen = Yen

    ## GETTER

    def getDivisaEur(self):
        return self.__DivisaEur
    def getDivisaDol(self):
        return self.__DivisaDol
    def getDivisaSol(self):
        return self.__DivisaSol
    def getDivisaMex(self):
        return self.__DivisaMex
    def getDivisaYen(self):
        return self.__DivisaYen
    
    
    ### METODO DE TASA DE CALCULO ?
    
    

