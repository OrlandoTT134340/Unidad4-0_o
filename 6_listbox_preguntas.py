#Orlando Escobedo Palafox
import tkinter as tk

def seleccionar():
    seleccion = listbox.curselection()
    if seleccion:
    # 2. Extrae el texto usando el primer índice [0]
     dato_seleccionado = listbox.get(seleccion[0]) 

     etiqueta.config(text=dato_seleccionado)

ventana = tk.Tk()
ventana.title("Preguntas")
ventana.configure(bg="brown") 

lista = ["Capital de alemania",
         "¿De quien es la cancion My generation?",
         "A quien pertenece la cancion TT?",
         "A quien pertenece la cancion what is love?",
         "A quien pertenece la cancion Gimme Chocolate?",
         "A quien pertenece la cancion boy with lov?"
         ]
listbox = tk.Listbox(ventana)
listbox.config(width=50,height=10)

listbox.insert(tk.END,*lista)
listbox.pack()


listbox.bind("<<ListboxSelect>>", lambda e:seleccionar())  

etiqueta = tk.Label(ventana)
etiqueta.config(width=50,height=10)
etiqueta.configure(bg="beige")
etiqueta.pack()





ventana.mainloop()