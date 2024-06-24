import time
import board
import busio
from adafruit_bmp280 import Adafruit_BMP280_I2C

# Crear un objeto I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Crear un objeto BMP280 utilizando la direcci�n I2C 0x76
bmp280 = Adafruit_BMP280_I2C(i2c, address=0x76)

# Configurar el modo de medici�n y otros par�metros si es necesario
bmp280.sea_level_pressure = 1013.25  # Presi�n al nivel del mar en hPa

try:
    while True:
        # Leer datos del BMP280
        temperatura = bmp280.temperature
        presion = bmp280.pressure
        altitud = bmp280.altitude

        # Imprimir los valores le�dos
        print(f"Temperatura: {temperatura:.2f} C")
        print(f"Presi�n: {presion:.2f} hPa")
        print(f"Altitud: {altitud:.2f} m")

        # Esperar un segundo antes de la pr�xima lectura
        time.sleep(1)

except KeyboardInterrupt:
    print("Lectura detenida por el usuario")
