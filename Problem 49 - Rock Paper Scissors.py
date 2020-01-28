# Problem #49 - Rock Paper Scissors http://www.codeabbey.com/index/task_view/rock-paper-scissors
# Submission by MPadilla - 04/Aug/2015


def prs(p1,p2):#Función paa comparar piedra-papel-tijeras y determinar un ganador.
    Winner=0
    if p1==p2:
        pass
    elif p1=="R":
        if p2=="S":
            Winner=1
        else:
            Winner=-1
    elif p1=="P":
        if p2=="R":
            Winner=1
        else:
            Winner=-1
    else:
        if p2=="R":
            Winner=-1
        else:
            Winner=1
    return(Winner)
        
    
print("Input number of games in the first lines, the games themselves. Each turn is separated by spaces:")
entr = [list(str(x) for x in input().split())for i in range(int(input()))]
N=len(entr) 

for i in range(N):
    win=0
    for j in range(len(entr[i])):
        win+=prs(entr[i][j][0],entr[i][j][1])
    if win > 0:
        entr[i]="1"
    else:
        entr[i]="2"

print("Winners of each game are:"," ".join(x for x in entr))
        
                
           
