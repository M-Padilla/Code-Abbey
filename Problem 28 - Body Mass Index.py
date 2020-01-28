# Problem #28 - Body Mass Index http://www.codeabbey.com/index/task_view/body-mass-index
# Submission by MPadilla - 20/Jul/2015


def bmi(weight, height): #Calcula el índice BMI y devuelve una calificación acorde.
    global entr
    index=weight/height**2
    if index<18.5:
        return "under"
    elif 18.5<=index<25.0:
        return "normal"
    elif 25.0<=index<30.0:
        return "over"
    else:
        return "obese"

N=int(input('How many people will you calculate BMI for?\n'))#Pregunta el numero de personas a las que se le calculará el BMI
print('Input the weight in kilograms and the height in meters of each person:')
entr = [(list(float(x) for x in input().split())) for i in range(N)] #Recibe los datos de peso y altura de cada individuo.
for i in range(N):
    entr[i]=bmi(entr[i][0], entr[i][1])#Para cada individuo, aplique función BMI
print("The BMI grade for each person are:"," ".join(str(x) for x in entr))
    

