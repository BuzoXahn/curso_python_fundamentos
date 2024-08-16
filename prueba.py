import pandas as pd
from openpyxl import Workbook 
import os
wb = Workbook()

archivo_excel = "Estadisticas.xlsx"


while True:
    print("\n\n\t\t*********--Bienvenido al Gestor de Estadisticas--***********\n\n")
    print("\t\t\t¿Qué quieres hacer?\n")
    print("\t\t\tElije una opción\n")
    print("\t\t\t**********************\n")
    print("\n'\t1. Agregar Jugador\n")
    print("\n'\t2. Buscar Jugador\n")
    res = int(input("\n'\t3. Actualizar Jugador\n"))
   
   
    if res == 1:   
        def guardar():
            global df
            nuevo = pd.DataFrame(columns=["Nombre","Número","Puntos","Partidos","Promedio","Rebotes","RE/Promedio","Asistencias","A/Promedio","Robos","RO/Promedio","Bloqueos","B/Promedio"])
                
            nuevo = nuevo.append({
                "Nombre": nom,
                "Número": num,
                "Puntos": pun,
                "Partidos": par,
                "Promedio": prom,
                "Rebotes": reb,
                "RE/Promedio": reprom,
                "Asistencias": asis,
                "A/Promedio": aprom,
                "Robos": rob,
                "RO/Promedio": roprom,
                "Bloqueos": bloq,
                "B/Promedio": bprom,

            })
            #df = pd.concat([df,nuevo], ignore_index=True)
            #df.to_excel(archivo_excel,sheet_name="Hoja1", index=False)
            nuevo.to_excel(archivo_excel,sheet_name="Hoja1", index=False)
        

        print("\n\n\tAgrega los siguientes datos")
        nom = input("\n\tNombre: ")
        num = int(input("\n\tNúmero: "))
        pun = int(input("\n\tPuntos: "))
        par = int(input("\n\tPartidos: "))
        reb = int(input("\n\tRebotes: "))
        asis = int(input("\n\tAsistencias: "))
        rob = int(input("\n\tRobos: "))
        bloq = int(input("\n\tBloqueos: "))
        prom = int(pun/par)
        reprom = reb/par
        aprom = asis/par
        roprom = rob/par
        bprom = bloq/par
        guardar(nom,num,pun,par,prom,reb,reprom,asis,aprom,rob,roprom,bloq,bprom)
        print("\n---->El Jugador se agrego correctamente<------")
        input()
          

    elif res == 2:
        def buscar(bus):
            resultado = df[df["Nombre"] == bus]
            if not resultado.empty:
                return resultado
            else: 
                return "No existe el Jugador", bus
        bus= input("\n\tIngres el Nombre del Jugador: \n\t")
        df = pd.read_excel(archivo_excel, sheet_name="Hoja1")  
        print(buscar(bus))
        input()

    elif res == 3:
        print("\n*******En Construcción*********")
        input()

    else:
        os.system("cls")
#guardar(nom,num,pun,par,prom,reb,reprom,asis,aprom,rob,roprom,bloq,bprom)
'''elif not res.empty: 
        print("\n\tElige una opción válida")
        os.system("cls")'''