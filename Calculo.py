from Divisador import CreaDivisador

## La variable 2 o 'Va2' es una variable extra
## que agregue en caso de que la llegaramos a
## necesitar para procesar alguna parte del
## calculo

# Favor de no borrarla pero si no la necesitas, no la uses
# Cuando se termine el programa se borrara


class Calculador():
    
    ## CONSTRUCTOR
    def __init__(self, Euro, Dolar, Sol, PMexicano, Yen, Resultado, Va2):
        super().__init__(Euro, Dolar, Sol, PMexicano, Yen)
        self.__ResultCal = Resultado
        self.__Valor2 = Va2
        
    
    ## SETTER
    
    def setResultado(self, Resultado):
        self.__ResultCal = Resultado
    
    def SetVa2(self, Va2):
        self.__Valor2 = Va2