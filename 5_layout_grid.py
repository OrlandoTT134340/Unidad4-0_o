#layout_grid
#Crea una ventana donde tienes que ingresar, nombre, edad, correo 
# y tiene quie mostrarlos al final en un messagebox
#Orlando Escobedo Palafox
#15/11/26
import tkinter as tk
from tkinter import messagebox
def mostrar():
    try:
          edad = entry2.get()
          entero = int(edad)
    except ValueError:
                    messagebox.showerror(title="ERROR",message="Tiene que ingresar u numeroi entero en EDAD",)

    nombre = entry.get()
    correo = entry3.get()
    messagebox.showinfo(title="Guardado",message=f"El nombre es: {nombre} de {entero} años, su correo es {correo}")

 

ventana = tk.Tk()
ventana.title("layout_grid")
ventana.config(background="beige")
ventana.minsize(300,100)
                                                  #Nombre
etiqueta_nombre = tk.Label(ventana,text="Nombre")
etiqueta_nombre.grid(row=0, column=0)
 
entry = tk.Entry()
entry.grid(row=0,column=1)

                                                   #Edad
etiqueta_edad = tk.Label(ventana,text="Edad")
etiqueta_edad.grid(row=1, column=0)
 
entry2 = tk.Entry()
entry2.grid(row=1,column=1)
                                                   #Correo
etiqueta_edad = tk.Label(ventana,text="Correo")
etiqueta_edad.grid(row=2, column=0)
 
entry3 = tk.Entry()
entry3.grid(row=2,column=1)

boton = tk.Button(ventana,text="GUARDAR",command=mostrar)
boton.grid(row=3,column=1)

ventana.mainloop()