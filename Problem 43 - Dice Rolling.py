# Problem #43 - Dice Rolling http://www.codeabbey.com/index/task_view/dice-rolling
# Submission by MPadilla - 01/Aug/2015

from math import floor

print("In the first line, input the amount of dice rolls you will calculate. In the following ones, input the random numbers:")
entr=[float(input()) for x in range(int(input()))]
N=len(entr)

for i in range(N):#Para cada número aleatorio haga:
    entr[i]=floor(entr[i]*6)+1#Aplique fórmula explicada para generar un puntaje de un dado de 6 caras.

print("Dice rolls are:"," ".join(str(x) for x in entr))
