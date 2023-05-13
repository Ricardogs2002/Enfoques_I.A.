
"Filtro de paso bajo (Low-pass filter): Este filtro se utiliza para suavizar la señal y "
"eliminar componentes de alta frecuencia, manteniendo las componentes de baja"
"frecuencia. Ayuda a reducir el ruido y las fluctuaciones no deseadas."
#El módulo scipy.signal es una librería que proporciona herramientas para el análisis y 
#procesamiento de señales, como filtros, transformadas, ventanas, etc. Una señal es una 
#representación de una cantidad física que varía en el tiempo o el espacio, como el sonido, 
#la luz, la temperatura, etc.

#Un filtro es un sistema que modifica una señal de entrada para obtener una señal de salida
# con ciertas características deseadas. Por ejemplo, un filtro de paso bajo permite 
#pasar las frecuencias bajas de una señal y atenúa las frecuencias altas. 
#Esto puede ser útil para eliminar el ruido o suavizar la señal.

#Un filtro Butterworth es un tipo de filtro que tiene una respuesta en 
#frecuencia lo más plana posible en la banda de paso, es decir, 
#que no introduce ondulaciones o distorsiones en las frecuencias 
#que se quieren conservar. El filtro Butterworth se caracteriza 
#por su orden y su frecuencia de corte. El orden determina la pendiente o la rapidez 
#con la que el filtro atenúa las frecuencias fuera de la banda de paso.
# La frecuencia de corte es la frecuencia límite entre la banda de paso y la banda de atenuación.

#La función butter del módulo scipy.signal permite diseñar un filtro Butterworth 
#digital o analógico y devuelve los coeficientes del numerador y el denominador 
#del filtro. Estos coeficientes definen la función de transferencia del filtro, 
#que relaciona la señal de entrada con la señal de salida en el dominio de la frecuencia. 
#La función butter recibe como argumentos el orden del filtro, la frecuencia o las frecuencias 
#de corte, el tipo de filtro (paso bajo, paso alto, paso banda o rechaza banda) 
#y si se quiere un filtro analógico o digital.

#La función lfilter del módulo scipy.signal permite aplicar un filtro lineal de coeficientes 
#constantes a los datos a lo largo de un eje dado. Esta función recibe como argumentos 
#los coeficientes del numerador y el denominador del filtro y los datos a filtrar. 
#La función devuelve los datos filtrados. La función lfilter implementa un algoritmo 
#recursivo que usa una ecuación en diferencias para calcular la salida del filtro
# a partir de la entrada y los valores anteriores.

#La función freqz del módulo scipy.signal permite calcular la respuesta en frecuencia 
#de un filtro digital dado por los coeficientes del numerador y el denominador. 
#Esta función recibe como argumentos los coeficientes del numerador y el denominador 
#del filtro y el número o el vector de frecuencias a evaluar. La función devuelve 
#las frecuencias y los valores complejos correspondientes a la respuesta en frecuencia. 
#La respuesta en frecuencia indica cómo se comporta el filtro para cada frecuencia de entrada, 
#es decir, cuánto atenúa o amplifica cada componente frecuencial.


import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

# Definir una función para crear un filtro Butterworth de paso bajo
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs # frecuencia de Nyquist
    normal_cutoff = cutoff / nyq # frecuencia de corte normalizada
    b, a = butter(order, normal_cutoff, btype='low', analog=False) # coeficientes del filtro
    return b, a

# Definir una función para aplicar el filtro a los datos
def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order) # crear el filtro
    y = lfilter(b, a, data) # filtrar los datos
    return y

# Establecer los parámetros del filtro
order = 6 # orden del filtro
fs = 30.0 # frecuencia de muestreo (Hz)
cutoff = 3.667 # frecuencia de corte (Hz)

# Crear el filtro
b, a = butter_lowpass(cutoff, fs, order)

# Graficar la respuesta en frecuencia del filtro
w, h = freqz(b, a, worN=8000) # calcular la respuesta en frecuencia
plt.subplot(2, 1, 1) # crear una subfigura
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b') # graficar la magnitud en función de la frecuencia
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko') # marcar la frecuencia de corte
plt.axvline(cutoff, color='k') # trazar una línea vertical en la frecuencia de corte
plt.xlim(0, 0.5*fs) # establecer el límite del eje x
plt.title("Respuesta en frecuencia del filtro de paso bajo") # poner el título
plt.xlabel('Frecuencia [Hz]') # poner la etiqueta del eje x
plt.grid() # poner la cuadrícula

# Crear los datos para filtrar
T = 5.0 # duración de la señal (segundos)
n = int(T * fs) # número de muestras
t = np.linspace(0, T, n, endpoint=False) # vector de tiempo
# Señal compuesta por tres senoides de diferente frecuencia y amplitud
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

# Filtrar los datos y graficar el resultado
y = butter_lowpass_filter(data, cutoff, fs, order) # aplicar el filtro
plt.subplot(2, 1, 2) # crear otra subfigura
plt.plot(t, data, 'b-', label='datos') # graficar los datos originales
plt.plot(t, y, 'g-', linewidth=2, label='datos filtrados') # graficar los datos filtrados
plt.xlabel('Tiempo [seg]') # poner la etiqueta del eje x
plt.grid() # poner la cuadrícula
plt.legend() # poner la leyenda
plt.subplots_adjust(hspace=0.35) # ajustar el espacio entre las subfiguras
plt.show() # mostrar la figura
