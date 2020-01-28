# Problem #38 - Quadratic Equation http://www.codeabbey.com/index/task_view/quadratic-equation
# Submission by MPadilla - 30/Jul/2015

def roundto(number):
    """Round a number to the nearest integer.  
    """
    number=int(number+0.5-((number+0.5)%1))
    return number

print("Input coefficients from quadratic equations:")
entr = [list(int(x) for x in input().split())for i in range(int(input()))]
N=len(entr) #Determina cuántas ecuaciones son, calculando la longitud del vector de entrada de datos

for i in range(len(entr)):#Para cada ecuación haga
    A,B,C=entr[i][0],entr[i][1],entr[i][2]#Asignación de coeficientes A,B,C para cada ecuación, donde
                                          #A * x^2 + B * x + C = 0
    x= [(-B + (B**2 - 4*A*C)**0.5) / (2*A),(-B - (B**2 - 4*A*C)**0.5) / (2*A)]#Obtención de raíces de la ecuación cuadrática
    if any(isinstance(k,complex) == True for k in x):#Si hay algún número complejo en las raíces
        for j in range(2):
            x[j]='{:.0f}'.format(roundto(x[j].real))+'{:+.0f}'.format(roundto(x[j].imag))+"i"
            #Formatear cada raíz, aproximándola al entero más cercano, colocándole el símbolo positivo o negativo
            #y cambiando el formato a+bj for a+bi.
    else:
        x=[str(roundto(r)) for r in x]#Si no es así, o sea, ambas raíces son reales, aproximar al entero más cercano.
    entr[i]=" ".join(r for r in x) #Guardar las raíces en el vector entr.

print("The roots for each quadratic equation are:","; ".join(x for x in entr))


