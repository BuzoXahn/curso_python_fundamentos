altura = float(input("\n Ingresa tu estatura en metros: \n"))
peso = float(input("\n Ingresa tu peso en kilos \n"))

IMC = peso / altura **2

if(IMC < 18.5):
    print( "\n Tu IMC es de: ", (IMC) , "\n Estas falto de peso\n")
else:
    if(IMC >=18.5 and IMC < 24.9):
        print("\n Tu IMC es de: ", (IMC) , "\n Estas en tu peso ideal\n")
    else:
        if(IMC >= 24.9 and IMC <29.9 ):
            print("\n Tu IMC es de: ", (IMC) ,"\n Tienes Sobrepeso" )
        else: 
            print("\n Tu IMC es de: ", (IMC) , "\n Tienes Obesidad\n A correr")


