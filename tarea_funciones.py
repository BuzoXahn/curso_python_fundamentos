import math
def calcular_area_circulo(radio):
    return math.pi * (radio*radio)

resultado = calcular_area_circulo(4)
print(round(resultado,2))

resultado = calcular_area_circulo(33.78)
print(round(resultado, 2))

resultado = calcular_area_circulo(10)
print(round(resultado, 2))

resultado = calcular_area_circulo(45)
print(round(resultado,2))

