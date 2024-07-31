confirmacion = "si"
numero = 100
for x in range (2):
    persona = input("\n\t Nombre: ")
    correo = input("\n\t Correo: ")
    respuesta = str (input("\n Quieres confirmar tu resgistro?"))

    if confirmacion == respuesta:
        print("\nTu numero de corredor es: ", numero)
        numero += 1
        x +=1
    else:
        print("\n Entonces no corres")

print("\n Lo sentimos ya no hay lugares \n")