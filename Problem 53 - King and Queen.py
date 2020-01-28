# Problem #53 - King and Queen Dice http://www.codeabbey.com/index/task_view/king-and-queen
# Submission by MPadilla - 08/Aug/2015


def killzone(target,killer):
    column={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    from math import atan2, degrees
    i,kill=0,"N"
    while kill=="N" and i<=1:
        if target[i]==killer[i]:
            kill="Y"
        i+=1
    if kill=="N":
        op=abs(int(target[1])-int(killer[1]))
        ad=abs(column[target[0]]-column[killer[0]])
        ang=int(degrees(atan2(op,ad)))
        if ang==45:
            kill="Y"
    return(kill)

print("Input number of games in the first lines, the games themselves. Each turn is separated by spaces:")
entr = [list(str(x) for x in input().split())for i in range(int(input()))]
N=len(entr) 

for i in range(N):
    king,queen=entr[i][0],entr[i][1]
    entr[i]=killzone(king,queen)

print("Possible kill status are:"," ".join(x for x in entr)) 
    
