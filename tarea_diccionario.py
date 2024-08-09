libro = {"Titulo":"Azteca","Autor": "Gary Jennings","Genero": "Novela Historica"}
print(libro.get("Titulo"))

print(libro.keys())

print(libro.values())

libro.update ({"Año":"1980"})

print(libro)

libro.pop ("Año")

print(libro)

for k, v in libro.items():
    print("\nLa Clave es: ", k, "Y el Valor es:", v)
    print("\n\t<<<<<<<<<<<<<>>>>>>>>>>>>>")