import tkinter as tk
from tkinter import ttk

#Crea una ventana con un treeview
ventana = tk.Tk()
ventana.title("Ranking")
ventana.geometry("400x350")
ventana.configure(bg="brown")

tabla = ttk.Treeview(ventana, columns=("posicion","jugador","puntaje"), show="headings")


tabla.heading("posicion",text="Posicion")
tabla.heading("jugador",text="Jugador")
tabla.heading("puntaje",text="Puntaje")

tabla.column("posicion", width=50, anchor="center")
tabla.column("jugador", width=50, anchor="center")
tabla.column("puntaje", width=50, anchor="center")

tabla.insert("",tk.END, values=(1,"Moa",90))
tabla.insert("",tk.END, values=(2,"Suga",85))
tabla.insert("",tk.END, values=(3,"RM",70))
tabla.insert("",tk.END, values=(4,"Jimin",69))
tabla.insert("",tk.END, values=(5,"V",50))

tabla.pack()

ventana.mainloop()