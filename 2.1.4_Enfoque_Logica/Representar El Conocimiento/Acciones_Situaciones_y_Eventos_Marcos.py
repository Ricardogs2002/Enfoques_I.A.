"""
Los marcos son una técnica útil y versátil para representar el conocimiento en términos de acciones, situaciones 
y eventos. Se utilizan en una amplia variedad de aplicaciones en inteligencia artificial y en el procesamiento 
del lenguaje natural, y pueden ser utilizados para modelar la estructura temporal de las acciones y eventos, así 
como para construir sistemas de planificación y toma de decisiones
"""
import matplotlib.pyplot as plt  # Importamos la biblioteca Matplotlib para crear gráficos

class Partido:
  def __init__(self, local, visitante, marcador, asistentes):
    self.local = local  # Atributo que representa el nombre del equipo local
    self.visitante = visitante  # Atributo que representa el nombre del equipo visitante
    self.marcador = marcador  # Atributo que representa el marcador del partido (una lista con los goles de cada equipo)
    self.asistentes = asistentes  # Atributo que representa el número de asistentes al partido

  def mostrar_resultado(self):
    plt.bar([self.local, self.visitante], [self.marcador[0], self.marcador[1]])  # Crear un gráfico de barras con los nombres de los equipos en el eje X y los goles en el eje Y
    plt.title("Resultado del partido")  # Agregar un título al gráfico
    plt.xlabel("Equipo")  # Etiquetar el eje X con "Equipo"
    plt.ylabel("Goles")  # Etiquetar el eje Y con "Goles"
    plt.show()  # Mostrar el gráfico en la pantalla

partido = Partido("Barcelona", "Real Madrid", [2, 1], 95000)  # Crear un objeto Partido con los atributos especificados
partido.mostrar_resultado()  # Llamar al método mostrar_resultado para mostrar el gráfico del resultado del partido
"""
En este ejemplo, definimos una clase Partido con los atributos local, visitante, marcador y asistentes. Luego, creamos 
un método mostrar_resultado que crea un gráfico de barras utilizando los datos del partido y lo muestra en la pantalla.

Finalmente, creamos un objeto Partido y llamamos al método mostrar_resultado para ver el gráfico del resultado del partido. 
Este es solo un ejemplo básico de cómo se pueden utilizar los marcos en Python para representar acciones, situaciones y 
eventos, y cómo se pueden visualizar mediante gráficos.
