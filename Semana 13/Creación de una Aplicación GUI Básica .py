import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Clik Aquí", "No te rindas ¡Tú puedes!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de GUI con Tkinter")
ventana.geometry('400x400')

# Crear un botón
boton = tk.Button(ventana, text="Clik Aquí", command= mostrar_mensaje)
boton.pack(pady=20)

# Ejecutar el bucle de eventos
ventana.mainloop()