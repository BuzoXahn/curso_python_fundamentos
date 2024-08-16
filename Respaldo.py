import pandas as pd
from openpyxl import Workbook 
import os
wb = Workbook()

archivo_excel = "jugadores.xlsx"
def mostrar_menu():
    print("\n\n\t\t*********--Bienvenido al Gestor de Estadisticas--***********\n\n")
    print("\t\t\t¿Qué quieres hacer?\n")
    print("\t\t\t**********************\n")
    print("\n'\t1. Agregar Jugador\n")
    print("\n'\t2. Buscar Jugador\n")
    print("\n'\t3. Actualizar Jugador\n")
    
   
   

def cargar_jugador():
    if os.path.exists(archivo_excel): 
        df = pd.read_excel(archivo_excel, index_col=0)
        return df.to_dict("index")
    else:
        return{}

def guardar_jugador(jugadores):
    df = pd.DataFrame(jugadores).T 
    df.to_excel(archivo_excel, index=True) 
    print("Los datos se guardaron correctamente")

def crear_excel():
    if not os.path.exists(archivo_excel):
        df = pd.DataFrame([
        "Nombre", 
        "Numero", 
        "Puntos", 
        "Partidos", 
        "Promedio",
        "Rebotes",
        "RE/Promedio",
        "Asistencias",
        "A/Promedio",
        "Robos",
        "RO/Promedio",
        "Bloqueos",
        "B/Promedio"
        
    ])
    df.to_excel(archivo_excel, index=False)
    print("\n\t------>El Archivo Se Creo Correctamente<------")

def agregar_jugador(jugadores):
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
    if nom in jugadores:
        print(f"Jugador {nom} ya existe")
    else:
        jugadores [nom]={
        "Nombre": nom,
        "Numero": num,
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
        "B/Promedio":bprom
        }
        guardar_jugador(jugadores)
        print("\n---->El Jugador se agrego correctamente<------")

def buscar(jugadores):
    nom = input("Ingrese nombre del Jugador")
    if nom in jugadores:
        estats = jugadores [nom]
        print(estats)
    else:
        return 
    print(f"El Jugador {nom} No Existe En La Base De Datos")

def actualizar(jugadores):
    nom = input("Ingresa nombre del jugador que vas actualizar")
    if nom in jugadores:
        puntos = input("Agregue los puntos")
        rebotes = input("Agregue los rebotes")
        asistencias = input("Agregue los asistencias")
        robos = input("Agregue los robos")
        bloqueos = input("Agregue los bloqueos")

        jugadores[nom]["Puntos"]+=puntos
        jugadores[nom]["Partidos"]+=1
        jugadores[nom]["Rebotes"]+=rebotes
        jugadores[nom]["Asistencias"]+=asistencias
        jugadores[nom]["Robos"]+=robos
        jugadores[nom]["Bloqueos"]+bloqueos      
        guardar_jugador(jugadores) 
        print("\n---->El Jugador se actualizó correctamente<------")
    else:
        print("-------->El Jugador No Existe<---------")
   
def main():
    crear_excel()
    jugadores = cargar_jugador
    while True:
        mostrar_menu()
        res = input("\t\t\tElije una opción\n")
        if res == "1":
            agregar_jugador(jugadores)
        elif res == "2":
            buscar(jugadores)
        elif res == "3":
            actualizar(jugadores)
            break
        else:
            print("Opción no válida")

if __name__=="__main__":
    main()
        

        
