#Ventana_basica
#Abre_una_ventan basica_con color y titulo
#Orlando Escobedo Palafox
#15/11/26
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.config(background="lightgray")
ventana.geometry("400x300")

ventana.mainloop()