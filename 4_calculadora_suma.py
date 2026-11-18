#calculadora_suma
#Crea una ventana que nos pide dos numeros para poder sumarlos
# y tiene excepcion por si ponen letras
#Orlando Escobeo Palafox
#15/11/26
import tkinter as tk 
def suma():
    try:
      num1 = entry.get()                     #Mandamos a traer nuestro resultado de entry
      num2 = entry2.get()
      decimal = float(num1)                  #convertimos en decimal(float)
      decimal2 = float(num2)                    #convertimos en decimal(float)
      suma = decimal + decimal2
      label3.config(text=suma)

    except ValueError:
     label3.config(text="Ingrese numeros")


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.minsize(200, 100) 

label = tk.Label(ventana,text="Numero 1")
label.pack()
entry = tk.Entry(ventana)
entry.pack()

labe2 = tk.Label(ventana,text="Numero 2")
labe2.pack()
entry2 = tk.Entry(ventana)
entry2.pack()


boton = tk.Button(ventana,text="Resultado",command=suma)
boton.pack()

label3 = tk.Label(ventana)
label3.pack()


ventana.mainloop()