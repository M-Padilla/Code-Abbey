# Problem #27 - Bubble Sort http://www.codeabbey.com/index/task_view/bubble-sort
# Submission by MPadilla - 20/Jul/2015

def swap():
    global entr,i
    cont=entr[i+1]
    entr[i+1]=entr[i]
    entr[i]=cont


N=int(input('How long is the array of numbers?\n'))#Pregunta el numero de elementos del vector
print('Input the array to sort:')
entr = list(int(x) for x in input().split()) #Recibe los elementos del vector a organizar.


totscount,passcount=0,0 #Inicializa iterador i, contador de intercambios y acumulador de checksum total.
unsorted=True #Crea variable de control booleana para señalar si el vector está desorganizado.

while unsorted==True: #Mientras el vector esté desorganizado
    swapcount=0 #Inicializa conteo de intercambios de la pasada
    for i in range(N-1):#Para cada par de elementos adyacentes del vector haga:
        if entr[i]>entr[i+1]: #Si el anterior es mayor al siguiente, intercambiar posiciones mediante función swap(), de tal manera que el mayor quede a la derecha
                              #y aumentar el contador de intercambios totales y de la pasada.
            swap()
            swapcount+=1
            totscount+=1
    if swapcount==0: #Si durante una pasada completa no se realizan intercambios quiere decir que ya el vector está organizado.
        unsorted=False
    passcount+=1#Actualiza conteo de pasadas realizadas.

print("Total number of passes performed and total swaps made are:",passcount,totscount)



