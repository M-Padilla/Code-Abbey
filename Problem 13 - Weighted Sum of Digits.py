# Problem #13 - Weighted sum of digits http://www.codeabbey.com/index/task_view/weighted-sum-of-digits
# Submission by MPadilla - 22/Jun/2015

def wsd(valor):#Función para calcular suma ponderada de digitos
    global entr,i
    suma=0 #Inicializa/Reinicia variable suma
    for j in range(len(entr[i])): #Para cada digito del numero hacer:
        suma+=(int(entr[i][j]))*(j+1) #Convierte en entero el digito, lo multiplica por su posición y lo suma. Se usa j+1 porque los vectores comienzan a contar de 0.
    entr[i]=suma #Asigna al elemento del vector el resultado de la suma ponderada

                
N=int(input('How many weighted sums of digits do you want to calculate?\n')) #Pregunta cuantas sumas ponderadas de digitos se desea calcular
print('Paste the input values here, in form of triplets A B C in order to calculate A*B+C and get the sum of its digits: ')
entr = [str(x) for x in input().split()] #Recibe las tripletas para calcular la suma de digitos y las transformar en strings para poder separar los digitos
for i in range(N):
    wsd(entr[i])#Aplica funcion wsd
print("The sums of the digits are: "+" ".join(str(x) for x in entr))
