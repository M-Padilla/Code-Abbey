# Problem #50 - Palindromes http://www.codeabbey.com/index/task_view/palindromes
# Submission by MPadilla - 08/Aug/2015


print("Input phrases number of phrases that will be evaluated whethere they are palindromes or not, the input the phrases themselves:")
entr = [str(x) for i in range(int(input())) for x in input().split("\n")] #Recibe las cadenas de caracteres enteras que dice el entero de la primera linea,
                                                                            #separadas por puntos apartes.
N=len(entr)

for i in range(N):#Para cada frase:
    entr[i]=entr[i].lower()#Vuelve todo minúsculas, para facilitar el análisis
    tstring=""#Inicializa cadena de prueba
    for char in range(len(entr[i])):#Examina cada caracter de la cadena, eliminando aquellos que no son letras, y agragando los que sí lo son a la cadena de prueba.
        if entr[i][char].isalpha()==True:
            tstring+=entr[i][char]
    if tstring==tstring[::-1]:#Si la cadena de prueba es igual a su reverso, o sea es una palíndrome:
        entr[i]="Y"#Asigna a la posicion de la palabra en el vector entr la letra "Y"
    else:
        entr[i]="N"#Asigna a la posicion de la palabra en el vector entr la letra "N"

print("Results of palidromes evaluations are:"," ".join(x for x in entr))
    
    
