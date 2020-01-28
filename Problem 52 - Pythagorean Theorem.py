# Problem #52 - Pythagorean Theorem Dice http://www.codeabbey.com/index/task_view/pythagorean-theorem
# Submission by MPadilla - 08/Aug/2015

from math import sqrt

def pyth(a,b):
    global c
    c=int("{:.0f}".format(sqrt(a**2+b**2)))
    return(c)

print("Input number of triangles in the first line and triangle sides in the following ones:")
entr = [list(int(x) for x in input().split())for i in range(int(input()))]
N=len(entr) 

for i in range(N):
    if pyth(entr[i][0],entr[i][1])==entr[i][2]:
        entr[i]="R"
    elif max(entr[i][0],entr[i][1],entr[i][2])<c:
        entr[i]="A"
    else:
        entr[i]="O"
        
print("Triangles are:"," ".join(x for x in entr))   
