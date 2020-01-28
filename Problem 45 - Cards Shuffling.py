# Problem #45 - Cards Shuffling http://www.codeabbey.com/index/task_view/cards-shuffling
# Submission by MPadilla - 01/Aug/2015

from math import floor

def swap(posa,posb):
    global deck
    deck[posa], deck[posb] = deck[posb], deck[posa]#Asignación simultánea de valores para intercambiar

print("Input position codes for swaps:")
entr = [int(x) for x in input().split()]

palo = ['C', 'D', 'H', 'S']
valor = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
deck=[i+j for i in palo for j in valor]#Genera un vector con el codigo palovalor, representando cada una de las 51 cartas. Ej 10 de Clubs, será TC.

for i in range(len(entr)):#Para cada código de posición:
    if entr[i]>51:#Si el código de posición es mayor a 51:
        entr[i]=entr[i]%52#Conviértelo a un núemro que este en el rango de las 52 cartas.
    swap(i,entr[i])#Ejecuta función swap para intercambiar posiciones
       
print("Shuffled cards:"," ".join(str(x) for x in deck))
