# Problem #10 - Linear Function http://www.codeabbey.com/index/task_view/linear-function
# Submission by MPadilla - 21/Jun/2015

def linearf(coord):#Función para calcular la pendiente A y el intercepto B de la función lineal
    global i,entr
    Xi=entr[i][0] 
    Xf=entr[i][2]
    Yi=entr[i][1]
    Yf=entr[i][3] #Selecciona cada punto inicial y final del cuarteto x1 y1 x2 y2
    A=int((Yf-Yi)/(Xf-Xi)) #Calcula la pendiente A y vuelve entero el valor.
    B=Yf-A*Xf #Toma una coordenada (la final en este caso), reemplaza y despeja para hallar el intercepto B
    entr[i]=(A,B) #Asignar pendiente A e intercepto B en un tuple
    entr[i]='('+" ".join(str(x) for x in entr[i])+')' #Vuelve el tuple una cadena de caracteres, los separa con espacios y los encierra con paréntesis.
                
N=int(input('How many linear functions will be found?\n')) #Pregunta cuantas funciones lineales serán halladas
print('Paste the input values here, in form of 4-tuples of values x1 y1 x2 y2')
entr = [(list(int(x) for x in input().split())) for i in range(N)] #Recibe las coordenadas y abscisas iniciales y finales para calcular las N funciones lineales
for i in range(N):
    linearf(entr[i])#Aplica funcion linearf
print("The slope A and intercept B for each linear function is: "+" ".join(str(x) for x in entr))
