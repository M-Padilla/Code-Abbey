# Problem #46 - Tic-Tac-Toe http://www.codeabbey.com/index/task_view/tic-tac-toe
# Submission by MPadilla - 04/Aug/2015

print("In the first line, input the number of games; in the following input the sequences of movements of each game, separated by spaces:")
entr = [list(str(x) for x in input().split())for i in range(int(input()))]
games=len(entr)
grid=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3))#Contiene las posiciones que conforman cada fila, columna, la diagonal y la antidiagonal
	#row de 1 a 3, col de 1 a 3, diagonal, y antidiagonal
        # 1 2 3
        # 4 5 6
        # 7 8 9

for i in range(games):#Para cada juego haga:
    scores,winplay=8*[0],0#Inicializa contador de puntajes para cada fila/columna/diagonal, y considera el juego por defecto como un empate hasta en
                          #caso se halle un ganador
    for j in range(9):#Para cada jugada del juego:
#Búsqueda
        turn=(-1)**j #Turno: 1 si es el turno de X, -1 si es el de O.
        matches=[(k, grid.index(int(entr[i][j]))) for k, grid in enumerate(grid) if int(entr[i][j]) in grid] #Encuentra todas las filas, columnas, diagonal y antidiag
        # que contengan a la jugada
        for k in range(len(matches)):#Para cada estructura que contenga la jugada:
            scores[matches[k][0]]+=turn #Actualiza el contador de puntaje de la estructura sumando 1 o -1 segun el jugador que realiza la jugada.
        if any(x in (3,-3) for x in scores):#Si en algún momento, alguno de los puntajes es 3 o -3, quiere decir qu alguien ha sido capaz de llenar una estructura
            #(una fila, una columna, diagonal o antidiagonal) completa y únicamente con sus jugadas, y por lo tanto ha logrado hacer triqui.
            winplay=j+1#Almacena la jugada en la cual se logro la victoria.
            break
#En caso que nadie gane, entonces la jugada ganadora se queda en 0, que simboliza empate.
    entr[i]=str(winplay)#Añade al vector entr la jugada ganadora

print("Victory (0 if Draw) at move:"," ".join(x for x in entr))

#--ENFOQUES ALTERNATIVOS--
#http://rowdy.msudenver.edu/~gordona/cs1050/progs/tictactoermccsc.pdf
#http://neverstopbuilding.com/minimax
#http://stackoverflow.com/questions/4198955/how-to-find-the-winner-of-a-tic-tac-toe-game-of-any-size
