import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin = 4

try:
    GPIO.setup(pin, GPIO.IN)
    print(f"El pin {pin} est� configurado correctamente como entrada.")
except Exception as e:
    print(f"Error al configurar el pin {pin}: {e}")
finally:
    GPIO.cleanup()
