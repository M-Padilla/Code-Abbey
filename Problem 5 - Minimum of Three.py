 # Problem #5 - Minimum of Three http://www.codeabbey.com/index/task_view/min-of-three
 # Submission by MPadilla - 15/Jun/2015

N=int(input('How many triplets of numbers are you gonna compare?\n')) #Pregunta cuantos trios se van a comparar
print('Paste the triplets of numbers here. Numbers of the same triplet must be separated by spaces; triplets must be separated by new lines:')
minimos = [(min(int(x) for x in input().split())) for i in range(N)] #Aplica comprension de lista. Crea una lista/vector de N elementos; cada N elemento es un vector
                                                                   #que contiene el trio de números. Estos se comparan y se selecciona el minimo, convirtiendose en
                                                                   #elementos individuales que constituyen el vector minimos.
print("The minimums of every triplet are the following: "+" ".join(str(x) for x in minimos)) ##Muestra los minimos de las N comparaciones de los trios, separados por espacios.


