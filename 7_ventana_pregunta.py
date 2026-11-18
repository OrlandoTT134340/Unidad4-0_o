

#objetos
#Orlando Escobedo Palafox

import tkinter as tk  # Importa la librería tkinter
from tkinter import messagebox


from pregunta_basica import Pregunta

def mostrar_pregunta_en_gui(pregunta_obj):
    top = tk.Toplevel()
    top.title("Ventana de Pregunta (Unidad 2)")
    top.geometry('300x250')
    top.config(bg='beige')
    

    tk.Label(top, text=pregunta_obj.texto, font=('Arial', 12, 'bold'), wraplength=350).pack(pady=15)
    
    tk.Label(top, text="Escribe tu respuesta:", font=('Arial', 10)).pack(pady=5)
    entrada_usuario = tk.Entry(top, font=('Arial', 11))
    entrada_usuario.pack(pady=5)

    def responder():
        respuesta = entrada_usuario.get()
        
        if pregunta_obj.verificar(respuesta):
            messagebox.showinfo("Resultado", "¡Respuesta Correcta!", parent=top)
        else:
            messagebox.showerror("Resultado", "Respuesta Incorrecta. Inténtalo de nuevo.", parent=top)

    # Botón para evaluar la respuesta
    tk.Button(top, text="Responder", command=responder).pack(pady=15)


# --- Código de prueba en la ventana principal ---
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana_pregunta")
    ventana_principal.geometry('360x300')
    ventana_principal.config(bg='violet')
    ventana_principal.attributes("-alpha",0.7)  

    mi_pregunta = Pregunta("¿Cual especie de animal es Tai lung?","leopardo")

    tk.Button(
        ventana_principal, 
        text="Abrir Pregunta", 
        font=('Arial', 11),
        command=lambda: mostrar_pregunta_en_gui(mi_pregunta)
    ).pack(expand=True)

    ventana_principal.mainloop()