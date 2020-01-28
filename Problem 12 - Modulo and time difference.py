# Problem #12 - Modulo and time difference http://www.codeabbey.com/index/task_view/modulo-and-time-difference
# Submission by MPadilla - 23/Jun/2015

def divfecha(fechas):#Función para calcular la diferencia de fecha
    global i,entr,dif
    dif,res=[0]*4,[0]*4 #Inicializa/Reinicia variable dif y res.
    for j in range(len(dif)):#Para cada unidad de tiempo haga:
        dif[j]=entr[i][j+4]-entr[i][j] #Restar la unidad de tiempo final menos la unidad de tiempo inicial (ej: day2-day1)
        #Condiciones para ajustar una diferencia negativa--
        if dif[j]<0: 
            if j!=1: #Si la unidad evaluada no está en horas haga:
                dif[j]+=60 #Calcular unidad de tiempo total ajustando con 60    
            else: #Si la unidad evaluada está en horas
                dif[j]+=24 #Calcular unidad de tiempo total ajustando para días
            res[j-1]-=1 #Si la diferencia es negativa para una unidad de tiempo, restarle a la unidad de tiempo inmediatamente mayor.
        #Conversion de segundos--
        if j==0: #Si la unidad de tiempo son días
            dif[j]*=24*(60**2)
        elif j!=3: #Si la unidad de tiempo no son ni días ni segundos
            dif[j]*=(60**(3-j))
    dif[3]=sum(dif) #Se suman todos los segundos y se asigna al elemento que contiene la unidad de tiempo de segundo.
    #Calculo con modulos de fechas
    for j in range(3, -1, -1): #Para cada unidad de tiempo haga:       
        if j>1:
            dif[j-1]=int(dif[j]/60)        
            dif[j]%=60
        elif j==1:
            dif[j-1]=int(dif[j]/24)
            dif[j]%=24
    #Suma cada elemento de res con su equivalente de posición en dif, ajustando las diferencias negativas.
    for j in range(len(res)):
        res[j]+=dif[j]  
    entr[i]=res
    entr[i]='('+" ".join(str(x) for x in entr[i])+')' #Vuelve la lista una cadena de caracteres, la separa con espacios y la encierra con paréntesis.
   
                                      
N=int(input('How many time differences do you need to calculate?\n')) #Pregunta cuantas diferencias de tiempo se calcularan
print('Paste the input values here, in form of 8-tuples of values day1 hour1 min1 sec1 day2 hour2 min2 sec2')
entr = [(list(int(x) for x in input().split())) for i in range(N)] #Recibe las N comparaciones de fechas, separa los octetos
                                                                    #de datos de cada uno, volviéndolos enteros y asignándolos a vector entr
for i in range(N): #Para cada caso
    divfecha(entr[i])#Aplica funcion divfecha
print("The time differences for each case are: "+" ".join(str(x) for x in entr))



