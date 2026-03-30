import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter

def main():
    root = tk.Tk()
    servicio = TareaServicio()
    app = AppTkinter(root, servicio)
    root.mainloop()

if __name__ == "__main__":
    main()