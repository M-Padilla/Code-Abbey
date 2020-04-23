 # Problem #6 - Rounding http://www.codeabbey.com/index/task_view/rounding
 # Submission by MPadilla - 21/Jun/2015

N=int(input('How many quotient of numbers are you gonna round?\n')) #Pregunta cuantos cocientes se van a aproximar
print('Paste the pairs of numbers here. Numbers of the same pair must be separated by spaces; pairs must be separated by new lines. The first number of a line is the numerator, the second one is the denominator:')
quo = [(list(int(x) for x in input().split())) for i in range(N)]#Aplica comprension de lista. Crea una lista/vector de N elementos; cada N elemento es un vector
                                                                  #que contiene el par de números, y se le aplica conversion a lista (vector)
for i in range(N):
        if ((quo[i][0]/quo[i][1])-(quo[i][0]//quo[i][1]))>=0.5: #Argumento para aproximar hacia arriba, comparando division normal con division de piso.
                quo[i]=1+(quo[i][0]//quo[i][1]) #Aproximación hacia arriba
        else: 
            quo[i]=(quo[i][0]//quo[i][1]) #Aproximación hacia abajo con division de piso.

print("The rounded quotients of the pairs are the following: "+" ".join(str(x) for x in quo)) #Muestra los resultados de los N cocientes aproximados de los pares, separados por espacios.

