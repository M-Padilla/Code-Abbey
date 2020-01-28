# Problem #23 - Bubble in Array http://www.codeabbey.com/index/task_view/bubble-in-array
# Submission by MPadilla - 17/Jul/2015

def checksum(valor):
    global entr,i,res
    res=((res+entr[i])*113)%10000007 #Ejecuta operación para calcular término de checksum y la adiciona a la variable que lleva la checksum total.

def swap():
    global entr,i
    cont=entr[i+1]
    entr[i+1]=entr[i]
    entr[i]=cont

print('Input the length of the array and the max range of the numbers in the array. Separate them with a space:')
entr = list(int(x) for x in input().split() if x!='-1') #Recibe las líneas de datos para calcular cada promedio e ignorando el -1 y usandolo
                                                        #como final de linea
i,swapcount,res=0,0,0 #Inicializa iterador i, contador de intercambios y acumulador de checksum total.

while i!=len(entr)-1: #Mientras no se examine el ultimo elemento haga:
    if entr[i]>entr[i+1]: #Si el elemento i es mayor que el elemento siguiente:
        swap()
        swapcount+=1
        i+=1   #Realizar intercambio, actualizar contador de intercambios y aumentar el iterador para examinar el siguiente elemento.   
    else: #Si no es asi, examinar el siguiente elemento.
        i+=1

for i in range(len(entr)): #Ejecuta función checksum para cada elemento del vector entr
    checksum(entr[i])

print('Swaps performed and Array checksum are respectively:',swapcount,res,sep=' ')

