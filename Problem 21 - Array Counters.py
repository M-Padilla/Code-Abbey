# Problem #21 - Array Counters http://www.codeabbey.com/index/task_view/array-counters
# Submission by MPadilla - 17/Jul/2015


#ATENCIÓN: El vector de números va de 1... N.

print('Input the length of the array and the max range of the numbers in the array. Separate them with a space:')
M,N=[int(x) for x in input().split()]
#Pregunta parametros M,N separados por un espacio. Donde M es el numero de elementos del vector, y N es el número tope dentro del vector. 
counters=N*[0] #Inicializa contadores para cada número menor o igual a N.
print('Paste the array of numbers:')
numbers=[int(x) for x in input().split()]
#Pide que se ingrese el vector de números separados por espacios

for i in range(0,N+1): #Para cada número, cuenta sus ocurrencias y las asigna a su espacio en el contador
    counters[i-1]=numbers.count(i)

print("The ocurrences for the sorted numbers are: \n"+" ".join(str(x) for x in counters))
