import tkinter as tk
from tkinter import ttk, messagebox

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")

        self.crear_widgets()
        self.cargar_tareas()

    def crear_widgets(self):
        # Campo de entrada
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        # Evento ENTER
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Botones
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Marcar Completada", command=self.completar_tarea).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_tarea).grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.tree = ttk.Treeview(self.root, columns=("Estado"), show="headings")
        self.tree.heading("Estado", text="Tareas")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Evento doble clic
        self.tree.bind("<Double-1>", self.completar_tarea_evento)

    def cargar_tareas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            if tarea.completado:
                texto += " [Hecho]"
            self.tree.insert("", "end", iid=tarea.id, values=(texto,))

    def agregar_tarea(self):
        descripcion = self.entry.get().strip()
        if descripcion == "":
            messagebox.showwarning("Aviso", "Ingrese una tarea")
            return

        self.servicio.agregar_tarea(descripcion)
        self.entry.delete(0, tk.END)
        self.cargar_tareas()

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def completar_tarea(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            return

        id_tarea = int(seleccionado[0])
        self.servicio.completar_tarea(id_tarea)
        self.cargar_tareas()

    def completar_tarea_evento(self, event):
        self.completar_tarea()

    def eliminar_tarea(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            return

        id_tarea = int(seleccionado[0])
        self.servicio.eliminar_tarea(id_tarea)
        self.cargar_tareas()