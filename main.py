"""
Ejercicio 3: Crear una clase llamada  ListaDeTareas  donde no va a recibir ningun argumento  en su constructor
pero va a tener un argumento  definido como una lista , y va a contener los siguientes metodos 

Metodos:
    -mostrarTareas()
    -agregarTareas(tarea)
    -quitarTareas(tarea)

"""


class ListaDeTareas():
  tareas = []

  def __init__(self):
    pass

  def mostrarTareas(self):
    return self.tareas
    #return ListaDeTareas.tareas

  def agregarTareas(self, tarea):
    self.tarea = tarea
    return self.tareas.append(self.tarea)

  def quitarTareas(self, tarea):
    self.tarea = tarea
    return self.tareas.remove(self.tarea)


tareas = ListaDeTareas()
tareas.agregarTareas("cocinar")
tareas.agregarTareas("jugar")
tareas.agregarTareas("estudiar")
tareas.agregarTareas("leer")
print(tareas.mostrarTareas())
tareas.quitarTareas("cocinar")
print(tareas.mostrarTareas())
