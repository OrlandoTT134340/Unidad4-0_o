#caja_texto
#Abre una ventana, con un boton y una caja para introducir texto
#Orlando Escobedo Palafox
#15/11/26
import tkinter as tk

def mostrar():
    texto = entry.get()
    label.config(text=texto)

ventana = tk.Tk()
ventana.minsize(200, 100) 

entry = tk.Entry(ventana)    #Entry es una caja donde se introduce una sola line a texto
entry.pack()

boton = tk.Button(ventana,text="Mostrar",command=mostrar)
boton.pack()

label = tk.Label(ventana)
label.pack()


ventana.mainloop()    