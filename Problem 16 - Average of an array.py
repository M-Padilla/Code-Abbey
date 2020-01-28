# Problem #16 - Average of an array http://www.codeabbey.com/index/task_view/average-of-array
# Submission by MPadilla - 25/Jun/2015

def avground(values):#FUnción para calcular promedio y redondear
    global i,entr
    #Suma de todos los datos de una línea
    suma=sum(entr[i])
    #Redondeo
    if ((suma/len(entr[i]))-(suma//len(entr[i])))>=0.5: #Argumento para aproximar hacia arriba, comparando division normal con division de piso.
                entr[i]=int(1+(suma/len(entr[i]))) #Aproximación hacia arriba
    else:
            entr[i]=int(suma/len(entr[i])) #Aproximación hacia abajo con division de piso.
    

N=int(input('How many averages will be calculated?\n')) #Pregunta cuantos promedios se calcularán
print('Paste the input, including 0 at the end of each line of data.')
entr = [(list(int(x) for x in input().split() if x!='0')) for i in range(N)] #Recibe las líneas de datos para calcular cada promedio e ignorando el 0 y usandolo
                                                                             #como final de linea
for i in range(N): #Para todas las líneas de datos haga:
    avground(entr)#Aplica función avg
    
print("The averages are the following: "+" ".join(str(x) for x in entr))

