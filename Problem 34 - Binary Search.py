# Problem #34 - Binary Search http://www.codeabbey.com/index/task_view/binary-search
# Submission by MPadilla - 24/Jul/2015


import math #Importa módulo math para llamar funciones sqrt y exp para calcula raiz cuadrada y e^x, respectivamente.

def eqsolve(xinitial,xfinal):#Funcion de busqueda binaria, cuyos argumentos son un valor de x inicial y uno final.
    global A,B,C,D
    tol=abs(xfinal-xinitial)#Define la tolerancia como el valor absoluto de la diferencia entre xfinal e initial, o sea el tamaño de segmento a analizar.
    while tol>=0.0000001:#Mientras que no se alcance suficiente precisión
        xm=(xinitial+xfinal)/2 #Xm es un valor intermedio que resulta del promedio de xfinal y initial
        result=(A*xm)+B*(math.sqrt(xm**3))-(C*(math.exp((-xm)/50)))-D #Reemplaza xm en la ecuación. El objetivo es hallar un x que hace que la ecuación sea 0.     
	if result>0:#Si el resultado es mayor que el objetivo, recortar la cota del segmento por la derecha, asignándole el valor de la mitad xm.
            xfinal=xm
        else:
            xinitial=xm #Si el resultado es menor que el objetivo, recortar la cota del segmento por la izquierda, asignándole el valor de la mitad xm.
        tol=xfinal-xinitial#Recalcula tolerancia
    return(round(xm,12))#Cuando finalmente alcanza la precision deseada, se devuelve el valor xm.


N=int(input('How many equations do you want to solve?\n'))#Pregunta cuantas ecuaciones se resolveran
print('Input the parameters for each equation, separated by spaces:')
entr = [list(float(x) for x in input().split()) for i in range(N)] #Recibe los coeficientes A,B,C,D de cada ecuación, separados por espacios.

for i in range(N):#Para cada ecuación:
	A,B,C,D=entr[i][0],entr[i][1],entr[i][2],entr[i][3]#Asigne parámetros
	entr[i]=eqsolve(0,100)#Aplique función eqsolve para búsqueda binaria y asgina su solución al vector entr.

print("The values of X that make the equation equal to zero for each set of parameters are:"," ".join(str(x) for x in entr),sep="\n")


#Este es el mismo método de Bisección de soluciones computacionales
