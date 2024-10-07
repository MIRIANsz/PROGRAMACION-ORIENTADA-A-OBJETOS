import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas Pendientes")
        self.root.geometry("400x400")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.entry_task = tk.Entry(root, width=40)
        self.entry_task.pack(pady=10)

        # Botones
        btn_add = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        btn_add.pack(pady=5)

        btn_complete = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        btn_complete.pack(pady=5)

        btn_delete = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        btn_delete.pack(pady=5)

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Asociar atajos de teclado
        root.bind('<Return>', lambda event: self.add_task())  # Enter para añadir tarea
        root.bind('<c>', lambda event: self.complete_task())  # 'C' para completar tarea
        root.bind('<Delete>', lambda event: self.delete_task())  # Supr para eliminar tarea
        root.bind('<d>', lambda event: self.delete_task())  # 'D' para eliminar tarea
        root.bind('<Escape>', lambda event: self.root.quit())  # Escape para cerrar la aplicación

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_task_index)
            if not task_text.startswith("[Completada]"):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, "[Completada] " + task_text)
            else:
                messagebox.showinfo("Info", "La tarea ya está completada.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


# Crear la ventana raíz
root = tk.Tk()
app = TaskManager(root)
root.mainloop()
