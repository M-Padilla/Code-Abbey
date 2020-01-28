# Problem #14 - Modular Calculator http://www.codeabbey.com/index/task_view/modular-calculator
# Submission by MPadilla - 23/Jun/2015

print("Input data for the calculations. First number is the initial value, the other ones are the operations. Hit 'Enter' twice once you're done with the input:")
entr = [] #Crea lista vacía entr
while True:
    line = input() #Toma una línea que el usuario introduce y lo asigna a la variable line
    if line: #Si la línea tiene contenido:
        entr.append(line) #Agregar a la lista entr, la cadena que está en line
    else: #Si la línea está vacía:
        res=int(entr[0]) #Significa que ya se acabó de introducir los datos y se interrumpe el while. Entonces se toma el primer elemento de entr y se asigna como el valor sobre el cual
                         #se ejecutarán las operaciones
        break
for i in range(1,len(entr)): #Para todos los valores que están después del valor inicial
    #Examinar el signo de operación que tiene la cadena, extraer el número y realizar el cálculo, asignándolo a la variable res.
    if entr[i][0]=='*': 
        res*=int(entr[i][2:])
    elif entr[i][0]=='+':
        res+=int(entr[i][2:])
    else:
         res%=int(entr[i][2:])   
print('The result of the calculations is',res)

