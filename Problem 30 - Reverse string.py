# Problem #30 - Reverse String http://www.codeabbey.com/index/task_view/reverse-string
# Submission by MPadilla - 20/Jul/2015

entr=input('Input the array with elements separated by spaces:\n') #Pide la frase a invertir
l,reverse=len(entr),"" #Calcula la longitud de la frase y crea una cadena sin contenido para almacenar la frase invertida.
for i in range(l,0,-1):#Desde el último elemento hasta el primero de la cadena de entrada, agregarlo a la cadena reverse; esto efectivamente invierte la cadena.
    reverse=reverse+entr[i-1]
print("The reversed string is:",reverse,sep='\n')  
