# Problem #42 - Blackjack Counting http://www.codeabbey.com/index/task_view/blackjack-counting
# Submission by MPadilla - 31/Jul/2015

entr = [list(str(x) for x in input().split())for i in range(int(input()))]
N=len(entr) #Determina cuántas manos de Blackjack se contarán.
valueten=("T","J","Q","K") #Crea vector de aquellas cartas cuyo valor es 10.

for i in range(N):#Para cada mano haga:
    score, aces=0,0#Inicializa contadores de puntaje y ases
    for j in range(len(entr[i])):#Para cada carta de la mano:
        if entr[i][j].isdigit():
            score+=int(entr[i][j])#Si es un dígito, convertir a entero y sumarlo al puntaje.
        elif entr[i][j] in valueten:
            score+=10#Si es alguna de las cartas que vale 10, sumarle 10 al puntaje.
        else:#Si es un as, incrementar la cuenta de ases y sumarle 11 al puntaje.
            aces+=1
            score+=11
        
    #Como un as puede tomar valor de 11 o 1, se realiza lo siguiente para ajustar los valores:
    
    while aces!=0 and score>21:#Mientras que la cuenta de aces sea  mayor a 0 y el puntaje exceda 21:
        score-=10 #Ajustar el valor del as bajándolo a 1, con el fin de actualizar el puntaje y ver si sigue excede 21.
        aces-=1 #Descontar el as que fue adjustado.
    
    if score<=21:#Si el puntaje es menor o igual a 21, asignar a entr el puntaje.
        entr[i]=str(score)
    else:
        entr[i]="Bust" #Si el puntaje es mayor que 21, asignar "Bust" a entr.

print("Countings are:"," ".join(x for x in entr))