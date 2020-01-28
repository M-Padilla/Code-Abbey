# Problem #26 - Greatest Common Divisor http://www.codeabbey.com/index/task_view/greatest-common-divisor
# Submission by MPadilla - 20/Jul/2015

def GCD(x,y):
    global gdiv
    while x and y: #Mientras que x y y sean diferentes de cero, el numero mayor se le sacaro el modulo respecto al menor y el resultado se asignara al mayor.
        if x>y:
            x%=y
        else:
            y%=x
    gdiv=max(x,y) #Asignar el valor que no sea cero como GCD  
    
def LCM(x,y):
    return(int((x*y)/gdiv)) #Usa la formula para despejar el LCM a partir del GCD
    
                
N=int(input('How many pairs are you gonna calculate GCD and LCM for?\n')) #Pregunta a cuantos pares se le calculara el MCD y el MCM
print('Paste the pairs here:')
entr = [(list(int(x) for x in input().split())) for i in range(N)] #Recibe los pares de numeros
for i in range(N):#Para cada par haga
    GCD(entr[i][0],entr[i][1]) 
    entr[i][1]=LCM(entr[i][0],entr[i][1])#Aplica funciones de GCD y LCM y las asigna
    entr[i][0]=gdiv
    entr[i]='('+" ".join(str(x) for x in entr[i])+')' #Convierte al formato (GCD LCM) de salida.

print("The slope A and intercept B for each linear function is: "+" ".join(str(x) for x in entr))



