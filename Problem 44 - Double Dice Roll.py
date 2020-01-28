# Problem #44 - Double Dice Roll http://www.codeabbey.com/index/task_view/double-dice-roll
# Submission by MPadilla - 01/Aug/2015

print("In the first line, input the amount of dice rolls you will calculate. In the following ones, input the random numbers for each dice, separated by spaces:")
entr = [list(int(x) for x in input().split())for i in range(int(input()))]
N=len(entr)

for i in range(N):#Para cada par de números aleatorios:
    for j in range(0,2):#Para cada número aleatorio
        entr[i][j]=(entr[i][j]%6)+1#Aplicar la fórmula para crear tiradas de dados a partir de números grandes.
    entr[i]=sum(entr[i])#Sumas ambas tiradas para obtener el total de los 2 dados.

print("Dice rolls are:"," ".join(str(x) for x in entr))
