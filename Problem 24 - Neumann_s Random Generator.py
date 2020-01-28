# Problem #24 - Neumann's Random Generator http://www.codeabbey.com/index/task_view/neumanns-random-generator
# Submission by MPadilla - 17/Jul/2015


def neumann(valor):
    global val,ite2loop,randomn
    randomn.append(val)#Agregar aleatorio generado al vector randomn para controlar recurrencia
    val=(int(val))**2 #Convertir a entero y elevar al cuadrado el número
    val=str(val) #Convertir a cadena para ejecutar lo sigte:
    if len(val)<8:  #Si la longitud de la cadena, o sea, el número tiene menos de 8 dígitos.
        val=(8-len(val))*'0'+val #Agregar tantos ceros a la izquierda como sea necesario para completar los 8 dígitos.
    val=val[2:6] #Truncar los 4 dígitos de la mitad. Este será el nuevo número aleatorio generado.  
    
N=int(input('How many seeds will you input?\n')) #Pide semillas del generador al usuario 
print('Input the seeds to generate random numbers - Range [0,9999]: ')
seed = [x for x in input().split()] #Recibe las semillas separadas por espacios

for i in range(N): #Para cada semilla haga
    val,randomn=seed[i],[] #Asigna la semilla a la variable val para poder operar. Crea un vector randomn, el cual tendrá los números aleatorios generados.
    ite2loop=0 #Inicializa contador de iteraciones hasta recurrencia.
    while (val in randomn)==False: #Mientras no haya recurrencia, es decir, que ningún número aleatorio generado se repita, haga:
        neumann(val)#Aplique función neumann.
        ite2loop+=1#Actualizar contador de iteraciones
    seed[i]=ite2loop #Almacena en el vector de semillas cuántas iteraciones se necesitaron para recurrencia.

print('Iterations until loop for each seed: '+" ".join(str(x) for x in seed))

