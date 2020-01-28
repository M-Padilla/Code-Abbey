# Problem #39 - Share Price Volatility http://www.codeabbey.com/index/task_view/share-price-volatility
# Submission by MPadilla - 31/Jul/2015


from statistics import mean, stdev

 
print("Input stock names and price records:")
entr = [list(str(x) for x in input().split())for i in range(int(input()))]
N=len(entr) #Determina cuántas acciones son.
deal=[]#Inicializa vector de acciones negociables segun el criterio de Paul.

for i in range(N):#Para cada acción
    for j in range(1,15):
        entr[i][j]=int(entr[i][j])#Convierte todo excepto el nombre en enteros, para poder calcular la media y desvest.
    praver,prstd=mean(entr[i][1:]),stdev(entr[i][1:])#Calcula media y desviación estandar del precio de la acción.
    comm=praver*0.01#Calcula la comisión del broker del 1% del precio promedio de la acción.
    if prstd/comm>=4:#Criterio de Paul: Si la desviación estandar del precio es al menos 4 veces mayor que el valor de la comisión, la acción se considera negociable.
        deal.append(entr[i][0])#Añadir el nombre de la acción al vector de acciones negociables.

print("Negotiable stocks accord to Paul's criteria:"," ".join(x for x in deal))
        
