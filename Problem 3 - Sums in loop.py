 # Problem #3 - Sums in Loop http://www.codeabbey.com/index/task_view/sums-in-loop
 # Submission by MPadilla - 15/Jun/2015

N=int(input('How many pair of numbers are you gonna sum?\n')) #Pregunta cuantos pares se van a sumar
print('Paste the pair of numbers here. Numbers of the same pairs must be separated by spaces; pairs must be separated by new lines:')
sumas = [(sum(int(x) for x in input().split())) for i in range(N)] #Aplica comprension de lista. Crea una lista/vector de N elementos; cada N elemento es un vector
                                                                   #que contiene el par de números. Estos se suman, convirtiendose en elementos individuales que
                                                                   #constituyen el vector sumas.
print("The sums of the pairs are the following: "+" ".join(str(x) for x in sumas)) #Muestra los resultados de las N sumas de los pares, separados por espacios.


