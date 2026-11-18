#15/11/26
#Orlando Escobedo Palafox

import tkinter as tk
from tkinter import messagebox
def mostrar():
    try:
          edad = entry2.get()
          entero = int(edad)
          
    except ValueError:
                    messagebox.showerror(title="ERROR",message="Tiene que ingresar un numero entero en EDAD",)

    nombre = entry.get()
    correo = entry3.get()
    while  True:
     if nombre == "" or nombre == "" and entero == "  " and correo == "  ":
                      messagebox.showerror(title="Advertencia",message=f"El nombre no puede estar vacio")
                      break
     if entero == "":
                messagebox.showerror(title="Advertencia",message=f"La edad no puede estar vacia")  
                break             
     if entero < 1 or entero > 120:
                       messagebox.showerror(title="ERROR",message="Su edad debe de ser un numero entre 1 y 120 ",)   
                       break  
     if correo.find("@"):  
                       messagebox.showerror(title="ERROR",message="Su correo debe de contener @ ",)    
                       break                
            
    
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