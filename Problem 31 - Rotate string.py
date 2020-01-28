# Problem #31 - Rotate String http://www.codeabbey.com/index/task_view/rotate-string
# Submission by MPadilla - 22/Jul/2015


N=int(input("How many strings will you rotate?\n"))
print("Input parameters, separated by spaces, to rotate string. First parameter is number of characters to rotate, second one is the string itself:")
entr =[(list(x for x in input().split())) for i in range(N)]#Recibe el número de caracteres a rotar y la cadena, por cada caso.
for i in range(N):#Para cada cadena a rotar, haga:
    if int(entr[i][0])>0:#Si el parámetro de rotación es positivo, llevar el numero de caracteres del principio al final
        entr[i]=(entr[i][1]+entr[i][1][:int(entr[i][0])])[int(entr[i][0]):]
    else:#Si el parámetro de rotación es negativo, llevar el numero de caracteres del final al principio
        entr[i]=(entr[i][1][int(entr[i][0]):]+entr[i][1])[:int(entr[i][0])]
        
print("Rotated strings are:"," ".join(x for x in entr),sep=' ')    
    



