# Problem #19 - Matching Brackets http://www.codeabbey.com/index/task_view/matching-brackets
# Submission by MPadilla - 17/Jul/2015


N=int(input('How many expressions will you check?\n'))#Pregunta a cuantas expresiones se les chequearán los paréntesis.
print('Paste the phrases:')
entr = [str(input()) for i in range(N)] #Recibe las expresiones separadas por puntos apartes
op,cl,opcl=('(','[','{','<'),(')',']','}','>'),('()','[]','{}','<>') #Tuples op, cl y opcl. op son los símbolos de apertura, cl los de cierre, y opcl son como se veria
                                                                        #un símbolo de apertura y cierre bien concatenado.
for i in range(N): #Para cada expresión haga:
        par=[] #Crea una lista vacía para guardar los símbolos de apertura
        check=1 #Asume que es correcta
        for j in range(len(entr[i])): #Para cada caracter en la expresión haga:
                if entr[i][j] in op: #Si es un símbolo de apertura, agregarlo a la lista par como si fuera un pendiente.
                        par.append(entr[i][j]) 
                elif entr[i][j] in cl: #Si es un símbolo de cierre:
                        if len(par)==0: #Si es un símbolo de cierre y no hay símbolo de apertura, la expresión está incorreta
                                check=0
                                break
                        elif par[-1]+entr[i][j] in opcl and len(par): #Comparar el símbolo de e con el último símbolo añadido a la lista par concatena correctamente
                                del(par[-1]) #Si es así se elimina el último elemento de par (como si se tachase el pendiente) 
                        else: #Si no concatena correctamente se rompe el ciclo de evaluación                                
                                break
                else:
                        continue
        if len(par)==0: #Si al terminar de evaluar la expresion no quedan pendientes en par, o sea que todo concatenó...
                entr[i]=check #Asignar a entr[i] el valor por defecto que es una expresión correcta
        else: #Si no concatena correctamente, se modifica a incorrecto el estado de la expresión y se asigna a entr[i]
                    check=0 
                    entr[i]=check
                    
print("The matching brackets evaluations for the expressions are (1 is correct, 0 is wrong): \n"+" ".join(str(x) for x in entr))

#La lógica del algoritmo para comparar se describe clara y gráficamente en http://www.davesquared.net/2008/07/brackets-braces-parenthesis-and-other.html
                        
                        
                        
                    
                        


                        
                      
           
