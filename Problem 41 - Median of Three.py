# Problem #41 - Median of Three http://www.codeabbey.com/index/task_view/median-of-three
# Submission by MPadilla - 31/Jul/2015


entr = [list(int(x) for x in input().split())for i in range(int(input()))]
N=len(entr) #Determina cuantas tripletas son.

for i in range(N):#Para cada tripleta haga:
    maxv,minv=max(entr[i]),min(entr[i])#Encuentra el m�ximo y el m�nimo.
    j=0#Inicializa contador de asignacion
    while ((entr[i][j]>minv) and (entr[i][j]<maxv))==False: #Mientras el n�mero que se examine no sea mayor que el minimo y menor que el m�ximo.
        j+=1#Aumenta el contador y exmaina el sigte n�mero
    entr[i]=entr[i][j]#Cuando se rompa el ciclo y se encuentre el n�mero que es la mediana, entonces reemplazarlo en el vector entr.

print("The medians of each triplet are:"," ".join(str(x) for x in entr))