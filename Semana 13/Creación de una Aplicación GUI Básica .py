import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Datos")

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Etiqueta para el campo de entrada
etiqueta = tk.Label(root, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto para la entrada de datos
entrada_dato = tk.Entry(root)
entrada_dato.pack(pady=5)

# Botón para agregar el dato
boton_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(root)
lista_datos.pack(pady=5)

# Botón para limpiar la lista
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la aplicación
root.mainloop()
