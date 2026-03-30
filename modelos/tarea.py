class Tarea:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        self.completado = False

    def marcar_completada(self):
        self.completado = True