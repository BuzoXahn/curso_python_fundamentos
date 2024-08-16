from tkinter import Tk, Label, Button, Entry
import openpyxl
import pandas as pd
from openpyxl import Workbook 
import tkinter.messagebox
wb = Workbook()

archivo_activo = wb.active

ventana = Tk ()
ventana.title("***Estadisticas del Jugador***")
ventana.geometry("850x450")

excel_writer = pd.ExcelWriter("Estadisticas.xlsx")


def guardado():

    dato1 = texto1.get()
    dato2 = texto2.get()
    dato3 = texto3.get()
    dato4 = texto4.get()
    dato5 = texto5.get()
    dato6 = texto6.get()
    dato7 = texto7.get()
    dato8 = texto8.get()
    dato9 = texto9.get()
    dato10 = texto10.get()
    dato11 = texto11.get()
    dato12 = texto12.get()
    dato13 = texto13.get()

    datos = pd.DataFrame({
        "Nombre del Jugador" : [dato1],
        "Numero del Jugador" : [dato2],
        "Puntos" : [dato3],
        "Partidos" : [dato4],
        "P/Partidos": [dato5],
        "Rebotes": [dato6],
        "P/Rebotes": [dato7],
        "Asistencias": [dato8],
        "P/Asistencias": [dato9],
        "Robos": [dato10],
        "P/Robos": [dato11],
        "Bloqueos": [dato12],
        "P/Bloqueos": [dato13]


    })


    
    datos.to_excel(excel_writer, sheet_name="Partido 1")
    excel_writer._save()

    texto1.delete(0,"end")
    texto2.delete(0,"end")
    texto3.delete(0,"end")
    texto4.delete(0,"end")
    texto5.delete(0,"end")
    texto6.delete(0,"end")
    texto7.delete(0,"end")
    texto8.delete(0,"end")
    texto9.delete(0,"end")
    texto10.delete(0,"end")
    texto11.delete(0,"end")
    texto12.delete(0,"end")
    texto13.delete(0,"end")

def cerrar():
    ventana.destroy()

    
def busqueda():
    bus = texto1.get()
    df=pd.read_excel(excel_writer)
    resultado = df[df["Nombre"] == bus]
    if not resultado.empty:
        return resultado
    else:
        return tkinter.messagebox.showinfo("ALERTA","No se encontró ese Jugador")



etiqueta1 = Label(ventana, text="Nombre", bg = "yellow",fg = "black", font=("Arial", 16))
etiqueta1.place(x=10, y=10, width=110, height=30)

texto1 = Entry(ventana, bg = "cyan",fg = "black", font=("Arial", 16))
texto1.place(x=130, y=10, width=200, height=30)

boton1 = Button(ventana, text="Guardar", bg = "orange", command= guardado, font=("Arial", 16))
boton1.place(x=450, y=10, width=100, height=30)

boton2 = Button(ventana, text="Borrar", bg = "orange", font=("Arial", 16))
boton2.place(x=600, y=10, width=100, height=30)

etiqueta2 = Label(ventana, text="Número", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta2.place(x=10, y=50, width=110, height=30)

texto2 = Entry(ventana, bg = "cyan",fg = "black", font=("Arial", 16))
texto2.place(x=130, y=50, width=200, height=30)

boton3 = Button(ventana, text="Buscar", bg = "orange", command = busqueda, font=("Arial", 16))
boton3.place(x=450, y=50, width=100, height=30)

boton4 = Button(ventana, text="Salir", bg = "orange", command = cerrar, font=("Arial", 16))
boton4.place(x=600, y=50, width=100, height=30)

etiqueta3 = Label(ventana, text="Puntos", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta3.place(x=10, y=120, width=110, height=30)

texto3 = Entry(ventana, bg = "cyan",fg = "black", font=("Arial", 16))
texto3.place(x=130, y=120, width=110, height=30)

etiqueta4 = Label(ventana, text="Partidos", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta4.place(x=260, y=120, width=110, height=30)

texto4 = Entry(ventana, bg = "cyan",fg = "black", font=("Arial", 16))
texto4.place(x=380, y=120, width=110, height=30)

etiqueta5 = Label(ventana, text="P/Promedio", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta5.place(x=510, y=120, width=110, height=30)

texto5 = Entry(ventana, bg = "cyan",fg = "black", font=("Arial", 16))
texto5.place(x=630, y=120, width=110, height=30)

etiqueta6 = Label(ventana, text="Rebotes", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta6.place(x=10, y=180, width=110, height=30)

texto6 = Entry(ventana, bg = "cyan",fg = "black", font=("Arial", 16))
texto6.place(x=130, y=180, width=110, height=30)

etiqueta7 = Label(ventana, text="P/Rebotes", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta7.place(x=260, y=180, width=110, height=30)

texto7 = Entry(ventana, bg = "cyan",fg = "black",font=("Arial", 16))
texto7.place(x=380, y=180, width=110, height=30)

etiqueta8 = Label(ventana, text="Asistencias", bg = "yellow",fg = "black", font= ("Arial", 14))
etiqueta8.place(x=10, y=240, width=110, height=30)

texto8 = Entry(ventana, bg = "cyan", fg = "black",font=("Arial", 16))
texto8.place(x=130, y=240, width=110, height=30)

etiqueta9 = Label(ventana, text="P/Asistencias", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta9.place(x=260, y=240, width=110, height=30)

texto9 = Entry(ventana, bg = "cyan", fg = "black", font=("Arial", 16))
texto9.place(x=380, y=240, width=110, height=30)

etiqueta10 = Label(ventana, text="Robos", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta10.place(x=10, y=300, width=110, height=30)

texto10 = Entry(ventana, bg = "cyan", fg = "black", font=("Arial", 16))
texto10.place(x=130, y=300, width=110, height=30)

etiqueta11 = Label(ventana, text="P/Robos", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta11.place(x=260, y=300, width=110, height=30)

texto11 = Entry(ventana, bg = "cyan", fg = "Black", font=("Arial", 16))
texto11.place(x=380, y=300, width=110, height=30)

etiqueta12 = Label(ventana, text="Bloqueos", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta12.place(x=10, y=360, width=110, height=30)

texto12 = Entry(ventana, bg = "cyan", fg = "Black", font=("Arial", 16))
texto12.place(x=130, y=360, width=110, height=30)

etiqueta13 = Label(ventana, text="P/Bloqueos", bg = "yellow",fg = "black", font= ("Arial", 16))
etiqueta13.place(x=260, y=360, width=110, height=30)

texto13 = Entry(ventana, bg = "cyan", fg = "Black",  font=("Arial", 16))
texto13.place(x=380, y=360, width=110, height=30)




ventana.mainloop()
