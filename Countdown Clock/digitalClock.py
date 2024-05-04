class DigitalClock():
    """Clase que muestra por pantalla un texto en formato digital
    00:00:00"""
    def __init__(self) -> None:
        self.__filas = ['', '', '']
        self.__numero = ''
        self.__numStr = ''
        self.__horas = ''
        self.__minutos = ''
        self.__segundos = ''
    
    def setTime(self, horas:int, minutos:int, segundos:int)->None:
        """Arma el tiempo (self.__numero) con las horas, minutos y segundos. 
        Pone 0s delante de un digito si es menor a 10"""
        self.__horas = str(horas)
        self.__minutos = str(minutos)
        self.__segundos = str(segundos)
        #Poner ceros delante de los numeros si son menores a 10
        if horas < 10:
            self.__horas = '0' + self.__horas
        if minutos < 10:
            self.__minutos = '0' + self.__minutos  
        if segundos < 10:
            self.__segundos = '0' + self.__segundos
            
        self.__numero = self.__horas + '*' + self.__minutos + '*' + self.__segundos
    
    def getNumber(self)->str:
        """El numero se compone de tres filas de un string. El número se va construyendo a
        partes, es decir la fila de arriba contiene las partes superiores de cada
        digito. Y asi sucesivamente con las partes de mitad e inferior"""
    
        
        for index, digito in enumerate(self.__numero):
            if digito == '0':
                self.__filas[0] += ' __ '
                self.__filas[1] += '|  |'
                self.__filas[2] += '|__|'
            elif digito == '1':
                self.__filas[0] += '    '
                self.__filas[1] += '   |'
                self.__filas[2] += '   |'
            elif digito == '2':
                self.__filas[0] += ' __ '
                self.__filas[1] += ' __|'
                self.__filas[2] += '|__ '
            elif digito == '3':
                self.__filas[0] += ' __ '
                self.__filas[1] += ' __|'
                self.__filas[2] += ' __|'
            elif digito == '4':
                self.__filas[0] += '    '
                self.__filas[1] += '|__|'
                self.__filas[2] += '   |'
            elif digito == '5':
                self.__filas[0] += ' __ '
                self.__filas[1] += '|__ '
                self.__filas[2] += ' __|'
            elif digito == '6':
                self.__filas[0] += ' __ '
                self.__filas[1] += '|__ '
                self.__filas[2] += '|__|'
            elif digito == '7':
                self.__filas[0] += ' __ '
                self.__filas[1] += '   |'
                self.__filas[2] += '   |'
            elif digito == '8':
                self.__filas[0] += ' __ '
                self.__filas[1] += '|__|'
                self.__filas[2] += '|__|'
            elif digito == '9':
                self.__filas[0] += ' __ '
                self.__filas[1] += '|__|'
                self.__filas[2] += '   |'
            elif digito == '*':
                self.__filas[0] += '   '
                self.__filas[1] += ' * '
                self.__filas[2] += ' * '
                
        self.__numStr = "\n".join(self.__filas)
        return self.__numStr
    