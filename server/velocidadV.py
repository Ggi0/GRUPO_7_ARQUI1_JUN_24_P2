import RPi.GPIO as GPIO
import time

# Definir el pin del fotointerruptor (número físico de pin)
PIN_FOTOINTERPTOR = 22  # GPIO 25

# Variables globales
contador_pulsos = 0
DISTANCIA_POR_PULSO = 0.1  # Ejemplo: 0.1 metros entre cada interrupción
TIEMPO_MEDICION = 1  # 1 segundo

def setup():
    """
    Configura los pines GPIO y la interrupción.
    """
    global contador_pulsos

    # Configurar el modo de numeración de pines
    GPIO.setmode(GPIO.BOARD)

    # Configurar el pin del fotointerruptor como entrada
    GPIO.setup(PIN_FOTOINTERPTOR, GPIO.IN)

    # Pausa corta para estabilizar el pin
    time.sleep(0.1)

    # Función de interrupción para contar los pulsos
    def contar_pulsos(channel):
        global contador_pulsos
        contador_pulsos += 1

    # Configurar la interrupción en el pin del fotointerruptor
    try:
        GPIO.add_event_detect(PIN_FOTOINTERPTOR, GPIO.FALLING, callback=contar_pulsos)
    except RuntimeError as e:
        print(f"Error al agregar detección de borde: {e}")
        GPIO.cleanup()
        exit(1)

def medir_velocidad():
    """
    Mide la velocidad en metros por segundo basada en los pulsos del fotointerruptor.
    """
    global contador_pulsos
    velocidad = 0

    try:
        while True:
            # Reiniciar el contador de pulsos
            contador_pulsos = 0

            # Esperar el tiempo de medición
            time.sleep(TIEMPO_MEDICION)

            # Calcular la velocidad (metros por segundo)
            velocidad = (contador_pulsos * DISTANCIA_POR_PULSO) / TIEMPO_MEDICION

            # Imprimir el resultado en la consola
            print(f"Velocidad: {velocidad:.2f} m/s")

            # Esperar un poco antes de la siguiente medición
            time.sleep(0.5)

    except KeyboardInterrupt:
        # Limpiar la configuración de GPIO al salir
        GPIO.cleanup()
        print("\nPrograma terminado.")

if __name__ == "__main__":
    setup()
    medir_velocidad()
