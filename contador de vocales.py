'''Inicio 
 Pedir al usuario que ingrese una cadena de texto y leer la cadena 
 inicializar el contador de vocales en cero 
 definir el conjunto de vocales: "aeiouAEIOU"
    Para cada caracter de la cadena
        Si el caracter está en el conjunto de vocales
  Incrementar el contador de vocales
        Fin Si
    Fin Para
    Escribir "El numero de vocales es: ", contador de vocales
Fin Inicio

'''


cadena= input("Ingrese un texto: ")
contador= 0
vocales= ("aeiouAEIOUáéíóúÁÉIÓÚ")
for x in cadena: 
    if x in vocales: 
         contador +=1
print ("Elnumero de vocales es: " + str(contador))

