# bandera de Noruega 

# se importa la libreria tkinter todas sus funciones
from tkinter import *

# Se crea una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto de tipo TK
ventana_principal = Tk()

# titulo de la ventana"
ventana_principal.title("Noruega Bandera")


# tamaño de la ventana
ventana_principal.geometry("1000x727")

# deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg = "firebrick4")

#--------------------
#frame entrda datos 
#--------------------
frame_blanco1 = Frame(ventana_principal)
frame_blanco1.config(bg = "white", width = 1000, height = 181)
frame_blanco1.place(x=0, y=272)

#--------------------
#frame entrda datos 
#--------------------
frame_blanco2 = Frame(ventana_principal)
frame_blanco2.config(bg = "white", width = 181, height = 727)
frame_blanco2.place(x=272, y=0)

#--------------------
#frame entrda datos 
#--------------------
frame_azul1 = Frame(ventana_principal)
frame_azul1.config(bg = "midnight blue", width = 90, height = 727)
frame_azul1.place(x=318, y=0)

#--------------------
#frame entrda datos 
#--------------------
frame_azul2 = Frame(ventana_principal)
frame_azul2.config(bg = "midnight blue", width = 1000, height = 90)
frame_azul2.place(x=0, y=318)

#se ejecuta el metodo mainloop() de la claseTk a través de la instancia (objeto) ventana_principa. 
# Este objeto despliega una ventana simple en pantalla y que a la espera de lo que el usuario haga
#  (click en el boton, escribir, etc.) cada accion del usuario se conoce como un evento el metodo mainloop 
# es un bucle infinito.

ventana_principal.mainloop()








