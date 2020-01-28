# Problem #15 - Maximum of array http://www.codeabbey.com/index/task_view/maximum-of-array
# Submission by MPadilla - 23/Jun/2015

def compv(valor):
    global entr,maxv,minv
    if maxv<entr[i]: #Si el valor máximo actual es superado por el elemento i del vector, este elemento es el nuevo máximo.
        maxv=entr[i]
    elif minv>entr[i]: #Si el valor mínimo actual supera al elemento i del vector, este elemento es el nuevo mínimo.
        minv=entr[i]

                
print('Input the array with elements separated by spaces: ')
entr=list([int(x) for x in input().split()]) #Recibe los valores separados por espacios
maxv,minv=entr[0],entr[0] #Toma el primer elemento del vector como valor inicial mínimo y máximo  
for i in range(1,len(entr)): #Ejecuta función compv para cada elemento del vector entr
    compv(entr[i])
    
print('The maximum value in the array is '+str(maxv)+' and the minimum value is '+str(minv))


