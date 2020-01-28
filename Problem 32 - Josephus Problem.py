# Problem #32 - Josephus Problem http://www.codeabbey.com/index/task_view/josephus-problem 
# Submission by MPadilla - 20/Jul/2015

import sys
print('Input how many people will be in the circle and the step to determine who will be killed, with a space between them:')
N,K=[int(x) for x in input().split()]#Recibe cuántas N personas integrarán el círculo y cuál K-ésimo miembro será eliminado.
defen=[x for x in range(1,N+1)#Crea un vector con las personas: Cada elemento contiene la posicion inicial.
index=0#Inicializa variable index
a=len(defen)#Inicializa contador de personas que aun viven.

while a!=1:#Mientras no haya un único sobreviviente haga:
    index+=K-1#Determinar que posición será la de la persona a eliminar.
              #Se resta 1 para ajustar el hecho que python considera la primera posición como posición 0.
    while index>=a:#Si la posición no corresponde al número de personas que están en el círculo.
        index-=a#Ajustar la posición al número de sobrevivientes, restándolo a index.
    del(defen[index])#Una vez determinado la posición, se procede a eliminarlo.
    a-=1

print("The safe position at the initial standing is",defen[0])        
    
    
    


