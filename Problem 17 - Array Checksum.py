# Problem #17 - Array Checksum http://www.codeabbey.com/index/task_view/array-checksum
# Submission by MPadilla - 23/Jun/2015

def checksum(valor):
    global entr,i,res
    res=((res+entr[i])*113)%10000007 #Ejecuta operación para calcular término de checksum y la adiciona a la variable que lleva la checksum total.

print('Input the array with elements separated by spaces: ')
entr=list([int(x) for x in input().split()]) #Recibe los valores separados por espacios
res=0
for i in range(len(entr)): #Ejecuta función checksum para cada elemento del vector entr
    checksum(entr[i])
    
print('Checksum calculated is',res)


