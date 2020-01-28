# Problem #33 - Parity Control http://www.codeabbey.com/index/task_view/parity-control
# Submission by MPadilla - 24/Jul/2015

#En este problema se usa paridad par.

print("Input message in encoded decimals separated by spaces.")
entr=(list(int(x) for x in input().split())) #Recibe el vector de los decimales codificados separados por espacios.
messagelength,i=len(entr),0 #Inicializa longitud del mensaje y contador

while i<messagelength:#Mientras no se haya llegado al final del mensaje
    a=bin(entr[i])#Convierte en binario en decimal, de la forma 0bXXXXX
    numbits=sum(int(x) for x in a[2:])#Suma los elementos a la izquierda de "b" en 0bXXXX para obtener el número de bits.
    if numbits in (2,4,6,8):#Si el número de bits es par:
        if len(a[2:])<8:#Si el número binario XXXXX es menor que 8, entonces el control de paridad es 0 y convertir a ASCII usando el valor codificado original. 
            entr[i]=chr(entr[i])#Esto es porque cuando el binario comienza por 0, Python lo recorta hasta el primer 1. Ej: 0b010 -> 0b10
        else:#Si el número binario XXXXX es 8, el octavo dígito es 1 del control de paridad, se desecha el digito de control y se convierte a ASCII desde su derecha.
            entr[i]=chr(int(a[3:],2))#Como se estaria seleccionando una cadena 0bXXXX (el output de bin()), se necesita aplicar conversion a entero primero.
        i+=1#Actualizar contador.
    else:#Si el número de bits es impar, entonces ocurrió corrupción de datos, ya que la suma de bits con el control de paridad se diseña para que siempre de par.
        del(entr[i])#Borrar caracter.
        messagelength-=1#Disminuir longitud del mensaje.

print(''.join(entr))
        

#Tabla de caracteres ASCII: http://ascii.cl/es/codigos-html.htm
#Explicación de Parity Check: http://www.techopedia.com/definition/1803/parity-check