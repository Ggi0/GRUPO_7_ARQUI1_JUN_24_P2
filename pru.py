import Adafruit_DHT
import time

# Configuraci�n del tipo de sensor y del pin GPIO al que est� conectado
sensor = Adafruit_DHT.DHT11
pin = 4  # Reemplaza con el pin GPIO que est�s usando

def leer_dht11():
    # Intenta obtener una lectura del sensor
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    
    if humedad is not None and temperatura is not None:
        print(f'Temperatura: {temperatura:.1f}�C')
        print(f'Humedad: {humedad:.1f}%')
    else:
        print('Fallo al obtener lectura del sensor. Intenta de nuevo!')

# Bucle principal
while True:
    leer_dht11()
    time.sleep(2)  # Espera 2 segundos antes de la pr�xima lectura

