#Para el codigo se utiliza un sensor de presencia y un actuador lineal

import RPi.GPIO as GPIO
import time

sensor_pin = 17 # El pin GPIO al que se conecta el sensor de proximidad
motor_pin = 18 # El pin GPIO al que se conecta el motor

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(motor_pin, GPIO.OUT)

while True:
    sensor_value = GPIO.input(sensor_pin) # Leer el valor del sensor
    if sensor_value == GPIO.HIGH: # Si el sensor detecta un objeto cercano
        GPIO.output(motor_pin, GPIO.HIGH) # Encender el motor
    else: # Si no se detecta ningún objeto cercano
        GPIO.output(motor_pin, GPIO.LOW) # Apagar el motor
    time.sleep(0.1)
