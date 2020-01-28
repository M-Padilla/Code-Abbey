# Problem #32 - Josephus Problem http://www.codeabbey.com/index/task_view/josephus-problem 
# Submission by MPadilla - 20/Jul/2015

import sys
print('Input how many people will be in the circle and the step to determine who will be killed, with a space between them:')
N,K=[int(x) for x in input().split()]#Recibe cu�ntas N personas integrar�n el c�rculo y cu�l K-�simo miembro ser� eliminado.
defen=[x for x in range(1,N+1)#Crea un vector con las personas: Cada elemento contiene la posicion inicial.
index=0#Inicializa variable index
a=len(defen)#Inicializa contador de personas que aun viven.

while a!=1:#Mientras no haya un �nico sobreviviente haga:
    index+=K-1#Determinar que posici�n ser� la de la persona a eliminar.
              #Se resta 1 para ajustar el hecho que python considera la primera posici�n como posici�n 0.
    while index>=a:#Si la posici�n no corresponde al n�mero de personas que est�n en el c�rculo.
        index-=a#Ajustar la posici�n al n�mero de sobrevivientes, rest�ndolo a index.
    del(defen[index])#Una vez determinado la posici�n, se procede a eliminarlo.
    a-=1

print("The safe position at the initial standing is",defen[0])        
    
    
    


