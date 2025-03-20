class GestorTareas:
    def __init__(self):
        """Inicializa una lista vacía de tareas."""
        self.tareas = []
        self.contador_id = 1  # ID autoincremental

    def agregar_tarea(self, nombre, descripcion):
        """Agrega una nueva tarea."""
        tarea = [str(self.contador_id), nombre, descripcion, "pendiente"]
        self.tareas.append(tarea)
        self.contador_id += 1

    def marcar_completada(self, tarea_id):
        """Marca una tarea como completada."""
        for tarea in self.tareas:
            if tarea[0] == str(tarea_id):
                tarea[3] = "completada"
                return
        return "No existe tarea para modificar"

    def marcar_en_progreso(self, tarea_id):
        """Marca una tarea en progreso."""
        for tarea in self.tareas:
            if tarea[0] == str(tarea_id):
                tarea[3] = "en progreso"
                return
        return "No existe tarea para modificar"

    def marcar_pendiente(self, tarea_id):
        """Marca una tarea como pendiente."""
        for tarea in self.tareas:
            if tarea[0] == str(tarea_id):
                tarea[3] = "pendiente"
                return
        return "No existe tarea para modificar"

    def eliminar_tarea(self, tarea_id):
        """Elimina una tarea por ID."""
        for tarea in self.tareas:
            if tarea[0] == str(tarea_id):
                self.tareas.remove(tarea)
                return
        return "No existe tarea para eliminar"

    def obtener_tareas_por_estado(self, estado):
        """Retorna todas las tareas en un estado específico."""
        tareas_filtradas = [
            tarea for tarea in self.tareas if tarea[3] == estado]
        return tareas_filtradas if tareas_filtradas else "Sin Tareas"
