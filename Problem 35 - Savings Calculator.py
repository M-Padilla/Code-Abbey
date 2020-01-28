# Problem #35 - Savings Calculator http://www.codeabbey.com/index/task_view/savings-calculator
# Submission by MPadilla - 24/Jul/2015

import math

def roundd(number,mult=0):
    return(math.floor(number*(10**mult))/(10**mult))#Usa la función floor del modulo math que redondea hacia abajo. La operacion entre parentesis
                                                    #es para lograr que la funcion se aproxime a los 2 cifras despues del decimal de los centavos.


N=int(input('How many cases will you calculate?\n'))
print('Input initial ammount S, required quantity R and interest P for each case, separated by spaces:')
entr = [list(int(x) for x in input().split()) for i in range(N)] #Recibe los datos separados por espacios

for i in range(N):
    S,R,P=entr[i][0],entr[i][1],1+(entr[i][2]/100) #Recibe el valor inicial de dinero S, el valor requerido R y el interés P;
                                                   #este último se transforma en decimal y se suma 1 para simplifcar los calculos al hacer R=S*(1+P)^T
    monacum,year=S,0 #Inicializa contador de dinero acumulado y años.
    while monacum<R:#Mientras no se reuna la cantidad deseada R:
        monacum=roundd(monacum*P,2)#Hacer efectivo el interes y redondear los centavos hacia abajo.
        year+=1#Sumar contador de años
    entr[i]=year#Cuando se reuna la cantidad, asignar el numero de años que tomó al vector entr.

print("The years required to get R from initial S under R interest rate for each case are:"," ".join(str(x) for x in entr))
