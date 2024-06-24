import RPi.GPIO as GPIO
import time

# Definir el pin del fotointerruptor (número físico de pin)
pinFotointerruptor = 22  # GPIO 25

# Variable para contar los pulsos
contador_pulsos = 0

# Definir la distancia entre las interrupciones (en metros)
# Ajusta esta distancia según la configuración de tu fotointerruptor
distancia_por_pulso = 0.1  # Ejemplo: 0.1 metros (10 cm) entre cada interrupción

# Tiempo de medición en segundos
tiempo_medicion = 1  # 1 segundo

# Velocidad resultante en m/s
velocidad = 0

# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BOARD)

# Configurar el pin del fotointerruptor como entrada
GPIO.setup(pinFotointerruptor, GPIO.IN)

# Función de interrupción para contar los pulsos
def contar_pulsos(channel):
    global contador_pulsos
    contador_pulsos += 1

# Configurar la interrupción en el pin del fotointerruptor
GPIO.add_event_detect(pinFotointerruptor, GPIO.FALLING, callback=contar_pulsos)

try:
    while True:
        # Reiniciar el contador de pulsos
        contador_pulsos = 0

        # Esperar el tiempo de medición
        time.sleep(tiempo_medicion)

        # Calcular la velocidad (metros por segundo)
        velocidad = (contador_pulsos * distancia_por_pulso) / tiempo_medicion

        # Imprimir el resultado en la consola
        print(f"Velocidad: {velocidad:.2f} m/s")

        # Esperar un poco antes de la siguiente medición
        time.sleep(0.5)

except KeyboardInterrupt:
    # Limpiar la configuración de GPIO al salir
    GPIO.cleanup()
    print("\nPrograma terminado.")

