# Problem #29 - Sort with Indexes http://www.codeabbey.com/index/task_view/sort-with-indexes
# Submission by MPadilla - 20/Jul/2015

N=int(input('How long is the array?\n'))#Pregunta el tamaño del vector de números
print('Input the array with elements separated by spaces:')
entr = (list(int(x) for x in input().split())) #Recibe el vector separado por espacios.
sort=sorted(entr) #Crea un nuevo vector en el que los elementos están organizados de menor a mayor.
for i in range(len(sort)):#Para cada elemento del vector organizado
    a=entr.index(sort[i]) #Busca cual fue la posicion del elemento del vector organizado sort en el vector de entrada entr y se le asigna.
    sort[i]=a+1
    entr[a]="-"#Como index encuentra la posicion de la primera ocurrencia del valor, esta raya sirve para prevenir confusiones en caso que hayan datos repetidos.
               #actuando como si se tacharan los elementos.

print("The sorted indexes are:"," ".join(str(x) for x in sort))
    

