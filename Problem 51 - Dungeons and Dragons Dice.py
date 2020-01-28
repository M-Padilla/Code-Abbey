# Problem #51 - Dungeons and Dragons Dice http://www.codeabbey.com/index/task_view/palindromes
# Submission by MPadilla - 08/Aug/2015

print("Input phrases number of phrases that will be evaluated whethere they are palindromes or not, the input the phrases themselves:")
entr = [list(int(x) for x in input().split() if int(x)!=0) for i in range(3)] #Recibe 3 series de totales de tiradas de dados
                                                                           

for i in range(3):
   ndices,sides=min(entr[i]),max(entr[i])//min(entr[i])  #El número de dados ndices se obtiene con el menor valor de las tiradas, es decir, el valor que da si todos los
                                                         #dados caen en 1 (4 dados darían una sumatoria de 4). El número de lados se obtiene dividiendo el maximo valor
                                                         #de las tiradas entre el número de dados (ej: si el puntaje fue 48 y son 4 dados, cada dado tiene 48//4= 12 lados)
   entr[i]=str(ndices)+"d"+str(sides)

print("Dices specs are:"," ".join(x for x in entr))
   

#ESTE PROBLEMA DEFINITIVAMENTE NO ES ASÍ, LA LOGICA ES COMO LA PLANTEE ORIGINALMENTE BUSCANDO EL VALOR TEORICO MAS APROXIMADO
