 # Problem #4 - Minimum of Two http://www.codeabbey.com/index/task_view/min-of-two
 # Submission by MPadilla - 15/Jun/2015

N=int(input('How many pair of numbers are you gonna compare?\n')) #Pregunta cuantos pares se van a comparar
print('Paste the pair of numbers here. Numbers of the same pairs must be separated by spaces; pairs must be separated by new lines:')
minimos = [(min(int(x) for x in input().split())) for i in range(N)] #Aplica comprension de lista. Crea una lista/vector de N elementos; cada N elemento es un vector
                                                                   #que contiene el par de números. Estos se comparan y se selecciona el minimo, convirtiendose en
                                                                   #elementos individuales que constituyen el vector minimos.
print("The minimums of every pair are the following: "+" ".join(str(x) for x in minimos)) #Muestra los minimos de las N comparaciones de los pares, separados por espacios.


