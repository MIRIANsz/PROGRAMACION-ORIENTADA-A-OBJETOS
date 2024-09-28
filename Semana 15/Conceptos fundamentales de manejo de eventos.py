import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x300")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task_event)  # Añadir tarea con la tecla Enter

        # Botones
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=35, height=10)
        self.task_listbox.pack(pady=10)

    def add_task_event(self, event):
        self.add_task()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"{task} - Completada")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
