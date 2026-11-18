#etiqueta_boton
#Abre una ventana, con un boton y un label que cambia si presionas el boton
#Orlando Escobedo Palafox
#15/11/26
import tkinter as tk
def cambiar_texto():
    label.config(text="Boton presionado")    

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.minsize(200, 100) 

label = tk.Label(ventana, text="Haz click en el boton")
label.pack()
boton = tk.Button(ventana, text="Cambiar",command=cambiar_texto)
boton.pack()

ventana.mainloop()