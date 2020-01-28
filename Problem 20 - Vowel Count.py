# Problem #20 - Vowel Count http://www.codeabbey.com/index/task_view/vowel-count
# Submission by MPadilla - 12/Jul/2015

def conteo(phrase):
    global entr, i
    countvow=0 #Inicializa o resetea contador de vocales
    for j in range(len(vowels)): #Para cada vocal
        countvow+=entr[i].count(vowels[j]) #Contar el número de ocurrencias en la frase entr[i]
                                           #y sumársela al contador
    entr[i]=countvow #Reemplazar el elemento entr[i] con la cuenta de sus vocales

N=int(input('How many phrases will you count?\n')) #Pregunta a cuantas frases se le contaran las vocales
print('Paste the phrases:')
entr = [input().lower() for i in range(N)] #Recibe las frases separadas por puntos y apartes y las convierte
                                            #en minusculas
vowels=['a','e','i','o','u','y'] #Define cuales son las vocales
for i in range(N): # A cada frase,
    conteo(entr[i])# Aplica función conteo

print("The vowel counts in each phrase are: "+" ".join(str(x) for x in entr))
