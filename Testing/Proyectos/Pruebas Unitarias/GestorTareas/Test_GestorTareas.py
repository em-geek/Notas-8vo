import unittest
from GestorTareas import GestorTareas


class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea('Tarea 1', 'Tarea de prueba')
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('pendiente'), [
                             ["1", "Tarea 1", "Tarea de prueba", "pendiente"]])

    def test_revisar_contador_tarea(self):
        self.gestor.agregar_tarea('Tarea 1', 'Tarea de prueba')
        self.gestor.agregar_tarea('Tarea rara', 'Tarea de prueba exprimental')
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('pendiente'), [
            ["1", "Tarea 1", "Tarea de prueba", "pendiente"],
            ["2", "Tarea rara", "Tarea de prueba exprimental", "pendiente"]])

    def test_marcar_tarea_completada(self):
        self.gestor.agregar_tarea('Tarea 1', 'Tarea de prueba')
        self.gestor.marcar_completada(1)
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('completada'), [
                             ["1", "Tarea 1", "Tarea de prueba", "completada"]])

    def test_marcar_tarea_en_progreso(self):
        self.gestor.agregar_tarea('Tarea 1', 'Tarea de prueba')
        self.gestor.marcar_en_progreso(1)
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('en progreso'), [
                             ["1", "Tarea 1", "Tarea de prueba", "en progreso"]])

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea('Tarea 1', 'Tarea de prueba')
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('pendiente'), [
                             ["1", "Tarea 1", "Tarea de prueba", "pendiente"]])
        self.gestor.eliminar_tarea(1)
        self.assertEqual(self.gestor.obtener_tareas_por_estado(
            'pendiente'), "Sin Tareas")

    def test_marcar_tarea_completada_a_pendiente(self):
        self.gestor.agregar_tarea('Tarea 1', 'Tarea de prueba')
        self.gestor.marcar_completada(1)
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('completada'), [
                             ["1", "Tarea 1", "Tarea de prueba", "completada"]])
        self.gestor.marcar_pendiente(1)
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('pendiente'), [
                             ["1", "Tarea 1", "Tarea de prueba", "pendiente"]])

    def test_marcar_tarea_en_progreso_a_pendiente(self):
        self.gestor.agregar_tarea('Tarea 1', 'Tarea de prueba')
        self.gestor.marcar_en_progreso(1)
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('en progreso'), [
                             ["1", "Tarea 1", "Tarea de prueba", "en progreso"]])
        self.gestor.marcar_pendiente(1)
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('pendiente'), [
                             ["1", "Tarea 1", "Tarea de prueba", "pendiente"]])

    def test_eliminar_tarea_inexistente(self):
        resultado = self.gestor.eliminar_tarea(1)
        self.assertEqual(resultado, "No existe tarea para eliminar")

    def test_modificar_tarea_inexistente_marca_completa(self):
        resultado = self.gestor.marcar_completada(1)
        self.assertEqual(resultado, "No existe tarea para modificar")

    def test_modificar_tarea_inexistente_marca_progreso(self):
        resultado = self.gestor.marcar_en_progreso(1)
        self.assertEqual(resultado, "No existe tarea para modificar")

    def test_modificar_tarea_inexistente_marca_pendiente(self):
        resultado = self.gestor.marcar_pendiente(1)
        self.assertEqual(resultado, "No existe tarea para modificar")

    def test_agregar_multiples_tareas(self):
        self.gestor.agregar_tarea('Tarea A', 'Descripción A')
        self.gestor.agregar_tarea('Tarea B', 'Descripción B')
        self.gestor.agregar_tarea('Tarea C', 'Descripción C')

        self.assertListEqual(self.gestor.obtener_tareas_por_estado('pendiente'), [
            ["1", "Tarea A", "Descripción A", "pendiente"],
            ["2", "Tarea B", "Descripción B", "pendiente"],
            ["3", "Tarea C", "Descripción C", "pendiente"]
        ])

    def test_eliminar_tarea_y_verificar_que_no_existe(self):
        self.gestor.agregar_tarea('Tarea Eliminada', 'Descripción')
        self.gestor.eliminar_tarea(1)
        self.assertEqual(self.gestor.obtener_tareas_por_estado(
            'pendiente'), 'Sin Tareas')
        self.assertEqual(self.gestor.obtener_tareas_por_estado(
            'completada'), 'Sin Tareas')
        self.assertEqual(self.gestor.obtener_tareas_por_estado(
            'en progreso'), 'Sin Tareas')

    def test_cambiar_estado_tarea_en_progreso_a_completada(self):
        self.gestor.agregar_tarea('Tarea Avance', 'Descripción')
        self.gestor.marcar_en_progreso(1)
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('en progreso'), [
                             ["1", "Tarea Avance", "Descripción", "en progreso"]])
        self.gestor.marcar_completada(1)
        self.assertListEqual(self.gestor.obtener_tareas_por_estado('completada'), [
                             ["1", "Tarea Avance", "Descripción", "completada"]])

    def test_modificar_estado_tarea_eliminada(self):
        self.gestor.agregar_tarea('Tarea Fantasma', 'Será eliminada')
        self.gestor.eliminar_tarea(1)
        self.assertEqual(self.gestor.marcar_completada(1),
                         "No existe tarea para modificar")
        self.assertEqual(self.gestor.marcar_en_progreso(1),
                         "No existe tarea para modificar")
        self.assertEqual(self.gestor.marcar_pendiente(1),
                         "No existe tarea para modificar")

    def test_obtener_tareas_devuelve_lista_vacia_si_no_hay_tareas(self):
        self.assertEqual(self.gestor.obtener_tareas_por_estado(
            'pendiente'), 'Sin Tareas')
        self.assertEqual(self.gestor.obtener_tareas_por_estado(
            'completada'), 'Sin Tareas')
        self.assertEqual(self.gestor.obtener_tareas_por_estado(
            'en progreso'), 'Sin Tareas')


if __name__ == '__main__':
    unittest.main()
