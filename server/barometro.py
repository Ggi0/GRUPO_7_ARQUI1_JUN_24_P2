import time
from bmp280 import BMP280  # Asumiendo que 'bmp280' es un módulo personalizado para BMP280
try:
    from smbus2 import SMBus  # Para Raspberry Pi 4, usar smbus2 es preferible
except ImportError:
    from smbus import SMBus  # Si smbus2 no está disponible, usar smbus

# Dirección del PCF8591 en el bus I2C
PCF8591_ADDRESS = 0x76

# Inicializar el bus I2C
bus = SMBus(1)

# Inicializar el BMP280
bmp280 = BMP280(i2c_dev=bus)

print("""temperature-and-pressure-with-adc.py - Displays the temperature, pressure, and analog input.

Press Ctrl+C to exit!
""")

def read_adc(channel):
    bus.write_byte(PCF8591_ADDRESS, (0x40 | channel))
    bus.read_byte(PCF8591_ADDRESS)  # Dummy read to start conversion
    return bus.read_byte(PCF8591_ADDRESS)

while True:
    try:
        # Leer temperatura y presión del BMP280
        temperature = bmp280.get_temperature()
        pressure = bmp280.get_pressure()

        # Leer valor ADC del PCF8591 (Canal 0)
        adc_value = read_adc(0)

        # Formatear la temperatura y la presión
        format_temp = "{:.2f}".format(temperature)
        format_press = "{:.2f}".format(pressure)

        # Mostrar resultados
        degree_sign = u"\N{DEGREE SIGN}"
        print('Temperature = ' + format_temp + degree_sign + 'C')
        print('Pressure = ' + format_press + ' hPa')
        print(f'Analog Input (ADC Channel 0) = {adc_value}')

        # Esperar antes de la próxima lectura
        time.sleep(4)

    except KeyboardInterrupt:
        print("\nLectura finalizada por el usuario.")
        break
    except Exception as e:
        print(f"Error: {e}")