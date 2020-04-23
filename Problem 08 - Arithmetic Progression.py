# Problem #8 - Arithmetic Progression http://www.codeabbey.com/index/task_view/arithmetic-progression
# Submission by MPadilla - 21/Jun/2015

def arith(prog):#Función para calcular progresión arirmética
    global i,entr
    A=entr[i][0] 
    B=entr[i][1]
    C=entr[i][2] #Selecciona de cada tripleta los parámetros respectivos A B y C
    prog=0
    for k in range(C): #Calculo iterado de los primeros valores y sumatorias
        prog+=A+(k*B)
    entr[i]=prog #Reemplazo del elemento del vector, por la sumatoria final de la progresión.
 
            
N=int(input('How many arithmetic progressions will be calculated?\n')) #Pregunta cuantas progresiones aritméticas se calcularan
print('Paste the input values here, in form of triplets of values A B N where A is the first value of the sequence, B is the step size and N is the number of first values which should be accounted.')
entr = [(list(int(x) for x in input().split())) for i in range(N)] #Recibe los parámetros de las progresiones, A es primer valor, B es el incremente, y N es el número
                                                                   #de primeros valores a calcular. 
for i in range(N):
    arith(entr[i])#Aplica funcion arith para calcular progresión aritmética
print("The arithmetic progressions calculated are the following: "+" ".join(str(x) for x in entr))

