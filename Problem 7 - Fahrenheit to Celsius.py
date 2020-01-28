# Problem #7 - Fahrenheit to Celsius http://www.codeabbey.com/index/task_view/fahrenheit-celsius
# Submission by MPadilla - 21/Jun/2015

def df2dcaprox(fah):#Función para convertir y aproximar a la vez
    global i,entr
    if ((5/9)/(1/(fah-32)))-(5/9)//(1/(fah-32))>=0.5: #Argumento para aproximar hacia arriba, comparando division normal con division de piso.
                entr[i]=1+((5/9)//(1/(fah-32))) #Aproximación hacia arriba
    else:
            entr[i]=((5/9)//(1/(fah-32))) #Aproximación hacia abajo con division de piso.
            

print('Paste the input values here. The first of them is the number of values to convert from Fahrenheit to Celsius: ')
entr = [int(x) for x in input().split()] #Recibe los valores pedidos
N=entr[0] #Toma el primer valor como el número de temperaturas a convertir
for i in range(1,N+1):
        df2dcaprox(entr[i])#Aplica funcion de conversión y aproximación df2dfaprox para cada valor del vector, omitiendo el # de temperaturas a convertir.

print("The conversions from Fahrenheit to Celsius are: "+" ".join(str(int(x)) for x in entr[1:]))  #Imprime las temperaturas convertidas y aproximadas, omitiendo el
                                                                                                        # de temperaturas a convertir.
        


