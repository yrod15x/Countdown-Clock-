from digitalClock import *
import os
from time import sleep

def soloNumerosPositivos(dato:str)->int:
    while True:
        try:
            entrada = int(input(f"Enter the {dato} >> "))
            if entrada >= 0:
                return entrada
            else:
                print("Data cannot be negative!")
        except ValueError:
            print("Invalid data!")
    return 0

def activarAlarma(horas:str, minutes:str, seconds:str)->str:
    """Devuelve un string por pantalla con los numeros digitales"""
    reloj = DigitalClock()
    reloj.setTime(horas, minutes, seconds)
    return reloj.getNumber()   
        

horas = soloNumerosPositivos('hours')
minutes = soloNumerosPositivos('minutes')
seconds = soloNumerosPositivos('seconds')

#las iteraciones del ciclo. Cada una cuenta como un segundo
num_seconds = (horas * 3600) + (minutes * 60) + seconds

for i in range(num_seconds):
    tiempo = activarAlarma(horas, minutes, seconds)
    print(tiempo)
    sleep(1)
    os.system('cls')
    seconds -= 1
    if horas == 0 and minutes == 0 and seconds == 0:
        print(tiempo)
        print('Suena Alarma')
        break
    if horas >= 0:
        if minutes <= 0 and seconds <= 0:
            minutes = 59
            horas -= 1 
        if minutes >= 0 and seconds < 0:
            seconds = 59
            minutes -=1
            
