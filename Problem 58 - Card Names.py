# Problem #58 - Card Names http://www.codeabbey.com/index/task_view/card-names
# Submission by MPadilla - 01/Aug/2015

from math import floor

N=int(input("Input number of cards:\n"))
print("Input card codes:")
entr = [int(x) for x in input().split()]

palo = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
valor = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


for i in range(N):#Para cada carta:
    palo_code=floor(entr[i]/13)#Aplica fórmula para hallar el código del palo de la carta.
    valor_code=entr[i]%13#Aplica fórmula para hallar el código del valor de la carta.
    
    palo_code=palo[palo_code]#Obten el nombre del palo en el vector palo
    valor_code=valor[valor_code]#Obten el valor de la carta en el vector valor.
    entr[i]=valor_code+"-of-"+palo_code#Asigna el valor y palo de la carta en el formato requerido.
      
       
print("Cards are:"," ".join(str(x) for x in entr))