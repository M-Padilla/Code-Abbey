# Problem #47 - Caesar Shift Cipher http://www.codeabbey.com/index/task_view/caesar-shift-cipher
# Submission by MPadilla - 04/Aug/2015

import string

print("Input number of sentences and key")
sentkey=[int(x) for x in input().split()]
print("Input sentences in uppercase and ending with .")
entr = [str(input()) for i in range(sentkey[0])] 
alp=tuple(string.ascii_uppercase)#Inicializa tuple que contiene letras del alfabeto en mayúsculas

#Este algoritmo descifra un mensaje cifrado con la clave del Cesar.

for i in range(sentkey[0]):#Para cada oración cifrada haga:
    decphr=""#Inicializa cadena descifrada
    for j in range(len(entr[i])-1):#Para cada caracter de la oración exceptuando el punto:
        if entr[i][j].isspace():#Si es espacio, se adiciona el espacio a la cadena descifrada
            decphr+=" "
        elif entr[i][j].isupper:#Si es una letra mayúscula, descrifa la letra yendose 3 letras más atrás y se adiciona la letra descifrada a la cadena descifrada.
                                #En caso de que se llegue al inicio del vector, se continua contando desde el último elemento.
            decoded=alp.index(entr[i][j])-sentkey[1]
            decphr+=alp[decoded]
    entr[i]=decphr+"."#Cuando se descifra toda se coloca el punto para señalar el fin de la cadena.

print("Decoded message:"," ".join(x for x in entr))
        
            

