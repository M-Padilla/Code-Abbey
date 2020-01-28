# Problem #22 - Two Printers http://www.codeabbey.com/index/task_view/two-printers
# Submission by MPadilla - 20/Jul/2015

D=int(input('How many documents will you print?\n')) #Pregunta cuántos documentos se imprimirán.
print('For each document, input the following info: Printer 1\'s Printing time per page, Printer 2\'s Printing time per page, Number of pages. Separate this with spaces')
entr = [(list(int(x) for x in input().split())) for i in range(D)] #Recibe los parámetros separados por espacios, y los documentos por punto y aparte

for i in range(D): #Para cada documento:
    X,Y,N=entr[i][0],entr[i][1],entr[i][2]#X y Y son los tiempos en que imprimen 1 página las impresoras 1 y 2 respectivamente. N es el número de páginas del documento
    mthtime=(X*Y*N)/(X+Y) #Calcula el tiempo mínimo teórico, despejando la ecuación N=A+B, donde A=(1/X)*t, B=(1/Y)*t que son el número de página impresas en función del
                          #tiempo óptimo para cada impresora y suponiendo que se pueden imprimir páginas parciales
    ppar1,ppar2=mthtime%X,mthtime%Y #Calcula el tiempo gastado en páginas parciales
    if ppar1 and ppar2: #Si se imprimieron páginas parciales, es decir si ppar1 y ppar2 !=0
        entr[i] = int(mthtime + min(X - ppar1, Y - ppar2)) #Le suma el menor tiempo que demoraría la impresora más rápida para imprimir la página parcial
                                                           #completamente, y luego aproxima hacia abajo para eliminar la página parcial de la otra impresora.
    else: #Sino, el tiempo minimo teorico es factible en la realidad y se asigna
          #tal cual como está al vector.
        entr[i] = int(mthtime)
        
print("The minimum possible times for each document are: "+" ".join(str(x) for x in entr))

#El primer algoritmo fue a fuerza bruta.
#Gracias a Yang Lei http://www.codeabbey.com/index/task_solution?task=two-printers&user=yang-lei&lang=Python
#La parte matemática del problema es explicada básicamente en http://dting.github.io/coding/two-printers/

