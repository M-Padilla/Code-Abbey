# Problem #18 - Square Root http://www.codeabbey.com/index/task_view/square-root
# Submission by MPadilla - 25/Jun/2015

def heron(value):
    global V, entr, i, R, d, T
    for t in range(T): #Calcula la aproximacion segun el método de Heron, pero sin usar tolerancia
        R=(R+d)/2
        d=V/R
    entr[i]=float(R)
        



N=int(input('How many square roots will be calculated?\n')) #Pregunta cuantas raices cuadradas se calcularán
print('Paste the input, where V=number you want to calculate the square root of; T=number of iterations.')
entr = [(list(int(x) for x in input().split())) for i in range(N)] #Recibe las líneas de datos para calcular cada aproximacion
for i in range(N):#Asignación de valores y aplica función heron.
        V,T=entr[i][0],entr[i][1]
        R=1
        d=V/R
        heron(V)
print("The square roots are the following: "+" ".join(str(x) for x in entr))



