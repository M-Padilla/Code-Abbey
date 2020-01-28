# Problem #11 - Sum of Digits http://www.codeabbey.com/index/task_view/sum-of-digits
# Submission by MPadilla - 22/Jun/2015

def sumdig(triplet):#Función para calcular suma de dígitos
    global i,entr
    A=entr[i][0]
    B=entr[i][1]
    C=entr[i][2] #Toma valores A, B y C de cada elementos del vector de valores.
    dig=str(A*B+C) #Calcula el resultado del cual se sumaran los digitos y lo vuelve una cadena para poder manipularla.
    end=len(dig)
    suma,j=0,0 #Inicializa/Reinicia variable suma, inicia contador de divisiones
    while j!=end: #Para cada digito del numero hacer:
        suma+=int(dig)%10#Divide el numero entre 10, y el residuo se asigna a la variable suma. Este residuo es el úlimo dígito del número.
        dig=dig[:-1]#Recorta el número hasta el penúltimo dígito.
        j+=1#Actualiza el contador de divisiones
        #Convertir en entero el dígito y sumárselo a la variable suma
    entr[i]=suma #La suma de los dígitos se asigna a la posición del vector, reemplazando la tripleta respectiva.

                
print('Input in the first line, how many sums of digits do you want to calculate and in the following lines paste the input values, in form of triplets A B C in order to calculate A*B+C and get the sum of its digits:')
#Pregunta cuantas sumas de digitos se desea calcular y pide los valores en sí.
entr = [list(int(x) for x in input().split())for i in range(int(input()))]
N=len(entr)

for i in range(N):
    sumdig(entr[i])#Aplica funcion sumdig

print("The sums of the digits are: "+" ".join(str(x) for x in entr))

