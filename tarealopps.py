contador = 0
frase = input("\n\t Introduzca una frase: ")
lista = frase.split ()
for apuntador in lista:
    contador +=1
print("\n\t El numero de palabras en tu frase es de:", contador)

indice = 0
frase = input("\n\t Introduzca una frase 2: ")
lista = frase.split (" ")
#print ("el numero de palabras en tu lista es de: ", len(lista))
while indice < len(lista):
         indice += 1 
print("\n\t El numero de palabras en tu frase es de:", indice)   
