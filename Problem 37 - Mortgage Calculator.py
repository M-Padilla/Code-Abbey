# Problem #37 - Mortgage Calculator http://www.codeabbey.com/index/task_view/mortgage-calculator
# Submission by MPadilla - 30/Jul/2015

import math

print("Input loan ammount P, yearly interest rate R and loan term L. Separate everything by spaces:")
entr = list(int(x) for x in input().split())
P,R,L=entr[0], (entr[1]/12)/100, entr[2]#Asignación de parámetros desde el vector de entrada de datos.
payment=math.ceil(P*(R*(1+R)**L)/((-1+(1+R)**L)))#Aplica fórmula para hallar pago mensual de hipotecas y redondea hacia el entero más cercano por arriba.
print("Required monthly payment for this loan is: "+str(payment))

#La fórmula para calcular el pago mensual se encuentra en http://www.wikihow.com/Calculate-Mortgage-Payments
