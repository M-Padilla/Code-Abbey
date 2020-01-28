# Problem #25 - Linear Congruential Generator http://www.codeabbey.com/index/task_view/linear-congruential-generator
# Submission by MPadilla - 20/Jul/2015


def lconggen(valor): #Ejecuta la fórmula del Generador Linear Congruencial hasta calcular el N-ésimo miembro de la secuencia
	global A,C,M,N
	for j in range(N):
		valor=(A*valor+C)%M
	return(valor)
  
    
N=int(input('How many sequences will you generate?\n')) #Pide cuántas secuencias se generarán
print('Input the parameters A, C, M, Xo, N to generate sequences, separated by spaces: ')
param = [(list(int(x) for x in input().split())) for i in range(N)] #Recibe los parámetros de las secuencias separados por espacios. N es el miembro que se desea
                                                                    #hallar, Xo es el número inicial para generar la secuencia. A, C y M son parámtros que se usan en
                                                                    #la fórmula del generador.
for i in range(N): #Para cada secuencia haga
	A,C,M,Xo,N=param[i][0],param[i][1],param[i][2],param[i][3],param[i][4] #Asigne parámetros a variables
	param[i]=lconggen(Xo) #Aplicar función del generador Lineal
	
print('The N-th members for each sequence are: '+" ".join(str(x) for x in param))

