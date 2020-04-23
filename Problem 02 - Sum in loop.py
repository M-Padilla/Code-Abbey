 # Problem #2 - Sum in Loop http://www.codeabbey.com/index/task_view/sum-in-loop
 # Submission by MPadilla - 15/Jun/2015

suma=0 #Inicializa la variable suma.
N=int(input('How many numbers are you gonna sum?\n')) #Pregunta la primera linea de input, cuantos numeros se sumaran

num=input('Paste the numbers you\'re gonna sum. There must be an space between numbers.\n').split() #Recibe los números a sumar, con un espacio entre ellos
                                                                                                    #y los asigna a un vector llamado num.
for x in range(N):
    suma+=int(num[x]) #Uso de Operadores de Asignación Aumentada. suma+= abrevia el escribir suma=suma+. La linea es sumar cada elemento del vector num
                      #a la variable sum. 
print('All that mess sums '+str(suma)) #Imprime el resultado de la suma
