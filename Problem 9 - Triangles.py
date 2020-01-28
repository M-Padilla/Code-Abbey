# Problem #9 - Triangles http://www.codeabbey.com/index/task_view/triangles
# Submission by MPadilla - 21/Jun/2015

def triatest(triangle):#Función para calcular progresión arirmética
    global i,entr
    list.sort(entr[i]) #Organiza los elementos de la lista de menor a mayor
    A=entr[i][0] 
    B=entr[i][1]
    C=entr[i][2] #Selecciona de cada triángulo los lados A B C, con C siendo el mayor.
    if (A+B)>=C: #Si la suma de dos lados es mayor o igual al tercero. NOTA: Un triángulo cuyos lados son iguales al tercero es posible pero tndria Área=0.
        entr[i]=1 #El triángulo es posible
    else:
        entr[i]=0 #El triángulo es imposible

            
N=int(input('How many triangles will be tested?\n')) #Pregunta cuantas triangulos serán examinados
print('Paste the input values here, in form of triplets of values A B C where each one is the length of a side.')
entr = [(list(int(x) for x in input().split())) for i in range(N)] #Recibe las longitudes A, B y C de los N triángulos.
for i in range(N):
    triatest(entr[i])#Aplica funcion triatest para comprobar la posibilidad de construir el triángulo
print("NOTATION:\nPossible Triangle: 1 - Impossible Triangle: 0.\nResults are the following for each proposed triangle:\n"+" ".join(str(x) for x in entr))

