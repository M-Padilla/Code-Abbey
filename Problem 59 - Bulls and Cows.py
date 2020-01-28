# Problem #59 - Bulls and Cows http://www.codeabbey.com/index/task_view/bulls-and-cows
# Submission by MPadilla - 23/Dic/2017

secret=input()[:4] #Toma el valor del # secreto
guesses=input().split() #Toma los # de las estimaciones
answer=[] #Crea el vector de las respuestas

for guess in guesses: #Para cada estimación
	bulls,cows=0,0 #Inicializa el contador de bulls y cows
	for _,i in zip(guess,range(4)): 
		#Para cada # y posición de las estimaciones,
		for number in secret: 
			if _ == number: #¿El # de la estimación coincide con alguno de los del #secreto?
				if i==secret.index(_): #¿El # de la estimación tiene exactamente la misma posición que el del # secreto?
					bulls+=1 #Sí, entonces es un bull
				else:
					cows+=1 #No, entonces es una cow.
	answer.append("-".join([str(bulls),str(cows)])) #Le da formato al resultado de la forma bulls-cows, los vuelve cadenas y los almacenas en el vector de respuestas para su posterior impresión

print(" ".join(answer))