import RPi.GPIO as GPIO
import time

# Definir el pin del fotointerruptor (n�mero f�sico de pin)
PIN_FOTOINTERPTOR = 40  # GPIO 21

# Variables globales
contador_pulsos = 0
DISTANCIA_POR_PULSO = 0.1  # Ejemplo: 0.1 metros entre cada interrupci�n
TIEMPO_MEDICION = 1  # 1 segundo

def setup():
    global contador_pulsos

    # Configurar el modo de numeraci�n de pines
    GPIO.setmode(GPIO.BOARD)

    # Configurar el pin del fotointerruptor como entrada con pull-up
    GPIO.setup(PIN_FOTOINTERPTOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Pausa corta para estabilizar el pin antes de configurar la interrupci�n
    time.sleep(0.1)

    # Funci�n de interrupci�n para contar los pulsos
    def contar_pulsos(channel):
        global contador_pulsos
        contador_pulsos += 1

    # Configurar la interrupci�n en el pin del fotointerruptor
    try:
        GPIO.add_event_detect(PIN_FOTOINTERPTOR, GPIO.FALLING, callback=contar_pulsos)
        print("Interrupci�n configurada correctamente.")
    except RuntimeError as e:
        print(f"Error al agregar detecci�n de borde: {e}")
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

            # Esperar el tiempo de medici�n
            time.sleep(TIEMPO_MEDICION)

            # Calcular la velocidad (metros por segundo)
            velocidad = (contador_pulsos * DISTANCIA_POR_PULSO) / TIEMPO_MEDICION

            # Imprimir el resultado en la consola
            print(f"Velocidad: {velocidad:.2f} m/s")

            # Esperar un poco antes de la siguiente medici�n
            time.sleep(0.5)

    except KeyboardInterrupt:
        # Limpiar la configuraci�n de GPIO al salir
        GPIO.cleanup()
        print("\nPrograma terminado.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        GPIO.cleanup()
        exit(1)

if __name__ == "__main__":
    setup()
    medir_velocidad()
