# Problem #48 - Collatz Sequence http://www.codeabbey.com/index/task_view/collatz-sequence
# Submission by MPadilla - 04/Aug/2015


def collatz(test):#Función para aplicar secuencia de Collatz.
    global number
    if (test%2) == 0:
            number=(test//2)
    else:
            number=(3*test+1)

cases=int(input("Input number of cases:\n"))
print("Input cases separated by spaces:")
entr=[int(x) for x in input().split()]            

for i in range(cases):#Para cada secuencia:
    number,itera=entr[i],0#Asigna el termino inicial como número e inicializa contador de iteraciones
    while number != 1:#Aplica función collatz hasta que el número se haga 1 y cuenta cada iteración necesaria
            collatz(number)
            itera+=1
    entr[i]=str(itera)


print("Steps for getting each Collatz Sequence to reach 1:"," ".join(x for x in entr),sep="\n")

