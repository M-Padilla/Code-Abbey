# Problem #40 - Paths in the Grid http://www.codeabbey.com/index/task_view/paths-in-the-grid
# Submission by MPadilla - 01/Aug/2015


print("Input grid's number of rows and column separated by spaces")
size=input().split()
rows=int(size[0])#Lee tamaño de la rejilla.
print("Input grid. @ is start, + are safe tiles, X are pits and $ is exit.")
entr = [list(str(x) for x in input().split())for i in range(rows)]#Lee la rejilla en sí con todos sus elementos.
currp,nextp=[[0,0]],[]#Inicializa las piscinas de la vectores de la generacion actual y siguiente, y coloca en la generacion actual el origen.
can,paths=[],0#Inicializa el vector que almacenas las coordenadas candidatas y el contador de caminos posibles.

#La lógica que sigue el problema es esta: Hay dos piscinas: Una actual (currp) y otra siguiente (nextp). Cada iteración examina las coordenadas actuales e intenta
#hacerlas avanzar hacia abajo y a la derecha (los unicos movimientos permitidos); si algun movimiento no se puede, la coordenada actual es eliminada, pero si es
#posible, las/la nueva coordenada se almacena en la piscina nextp. Al final de la iteración, nextp es la nueva currp y se repite hasta que no hayan más puntos desde
#donde moverse.

while len(currp)!=0:#Mientras haya puntos desde el cual moverse haga:
    for i in range(len(currp)):#Para cada punto de la piscina actual haga:
            for j in range(0,2):
                can=currp[i].copy()#Genera un movimiento a examinar, a la derecha (cuando j=1) o abajo (cuando j=0).
                can[j]+=1
                try:#Si el movimiento entra dentro de los límites de la rejilla:
                    if entr[can[0]][can[1]]!="$":#Si el movimiento no lleva a la salida:
                        if entr[can[0]][can[1]]=="+":#Revisa si el movimiento lleva entonces a una casilla segura; si es asi guarda la nueva coordenada en el vector
                                                    #nextp para la siguiente iteración. Si lleva a un abismo sencillamente se ignora el movimiento propuesto.
                            nextp.append(can)
                    else:#Si el movimiento lleva a la salida, se ha construido un camino posible y debe aumentarse el contador de caminos.
                        paths+=1
                except:#Si el movimiento se sale de los limites de la rejilla, se ignora.
                    pass
    currp=nextp.copy()#Una vez se han evaluado todas las posibilidades actuales, los movimientos hechos se vuelven las posiciones actuales
    nextp.clear()#y se limpia el vector para recibir los movimientos posibles de la siguiente iteración.

print("Total available paths in grid are:",paths)
