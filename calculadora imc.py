print("Esto es una calculadora de Indice de Masa Corporal")
Peso= float(input("¿Cual es tu peso? (kg)"))
Altura= float(input("¿Cual es tu altura? (mts)"))
IMC=Peso/(Altura **2)
print("Tu IMC es" , IMC)

if IMC <= 18.5:
    print("Bajo de Peso")
elif 18.5<= IMC < 24.9:
    print("Peso Normal")
elif 24.9 <= IMC < 29.9:
    print("Sobre Peso")
else: 
    print("Obesidad")
    

