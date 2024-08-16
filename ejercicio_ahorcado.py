import random
puntero = 0
intento= 0
#palabra_elegida():
lista = ["Escritorio", "Mouse", "Teclado", "Cable", "Silla", "Telefono","Bote", "Taza"]
palabra = random.choice(lista)
oculta = ["_"]*len(palabra)
    

def avance_juego():
    print ("Intentos restantes" , intento+3)
    print("Palabra: ", " ".join(oculta))



'''while intento < 3:
    letra = input("\n Pregunta una letra: ")
    if letra in juego:
        print("si esta esa letra ")
        busca = juego.split()
        if letra == busca.index(puntero):
            print(juego.index(puntero))
    else: 
        print("Esa letra no esta")
        print("\n Intento No:  ", intento+1)
    intento+=1'''






