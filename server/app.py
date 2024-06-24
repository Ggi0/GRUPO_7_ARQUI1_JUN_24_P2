
#* Los from son las librerias que vamos a utilizar en nuestro servidor pero solo algunas funciones de ellas
from flask      import Flask, request, jsonify
from flask_cors import CORS

# libreria para i2c
"""
from bmn280     import BMN280

#* Asumiendo que 'bmp280' es un módulo personalizado para BMP280
try:
#* # Para Raspberry Pi 4, usar smbus2 es preferible
    from smbus2 import SMBus  
except ImportError:
    from smbus  import SMBus  
"""
#* Los imports son las librerias que vamos a utilizar en nuestro servidor pero todas las funciones de ellas
import sys
import time

#* creamos una instancia de la clase Flask
app = Flask(__name__)
#* creamos una instancia de la clase CORS
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# ------------------------ DATOS LEIDOS --------------------------
datos = []


# ----------------------------VARIABLES ----------------------


#globales para sensor de calidad de aire

sensor_aire = False


#globales para sensor de temperatura
sensor_temp = False


#globales para sensor de humedad
sensor_humedad = False


#globales para luminosidad
sensor_luminosidad = False

#globales para sensor de viento
sensor_viento = False

#globales para sensor barometrico
sensor_barometrico = False



# ------------------------- DECLARACION DE PUERTOS---------------------------

#Pines GPIO 

#Sensor de calidad de aire digital
PIN_AIRE = 11          #GPIO 17

#Sensor Temperatura y humedad
PIN_TEMP = 17          #GPIO 4

#Sensor de velocidad viento
PIN_VIENTO = 22        #GPIO 25

#Sensor de luminosidad digital
PIN_LUZ = 13           #GPIO 17


# I2C
#Sensor de Calidad de aire I2C y de Luminosidad I2C
PCF8591_ADDRESS = 0x48
bus = smbus2.SMBus(1)

#Sensor de Presion Barometrica I2C

# Dirección del PCF8591 en el bus I2C
PCF8591_ADDRESS_Barometro = 0x76

# Inicializar el bus I2C
bus_Barometro = SMBus(1)

# Inicializar el BMP280
bmp280 = BMP280(i2c_dev=bus)

# ------------------------- FUNCIONES API ---------------------------


#* Funcion para encender el sensor seleccionado
@app.route('/api/on', methods=['POST'])
def On_Sensor():
    data = request.get_json()
    sensor = data.get('sensor')
    
    if sensor is None:
        return jsonify({'error': 'sensor and action are required'}), 400
    
    #* Aqui se debe de agregar la logica para encender el sensor
    if   sensor == '12':
        print("Sensor Temperatura encendido")  
    elif sensor == '13':
        print("Sensor Humedad encendido")
    elif sensor == '14':
        print("Sensor Velocidad viento encendido")
    elif sensor == '15':
        print("Sensor Luminosidad encendido")
        On_luminosidad()
    elif sensor == '16':
        print("Sensor Calidad de aire encendido")
    elif sensor == '17':
        print("Sensor Presion Barometrica encendido")
    else:
        return jsonify({'message': 'invalid sensor'}), 400
    
    return jsonify({'message': sensor})

#* Funcion para apagar el sensor seleccionado
@app.route('/api/off', methods=['POST'])
def Off_Sensor():
    data = request.get_json()
    sensor = data.get('sensor')
    
    if sensor is None:
        return jsonify({'error': 'sensor and action are required'}), 400
    
    #* Aqui se debe de agregar la logica para apagar el sensor
    if   sensor == '12':
        print("Sensor Temperatura apagado")  
    elif sensor == '13':
        print("Sensor Humedad apagado")
    elif sensor == '14':
        print("Sensor Velocidad viento apagado")
    elif sensor == '15':
        print("Sensor Luminosidad apagado")
        Off_luminosidad()
    elif sensor == '16':
        print("Sensor Calidad de aire apagado")
    elif sensor == '17':
        print("Sensor Presion Barometrica apagado")
    else:
        return jsonify({'message': 'invalid sensor'}), 400
    
    return jsonify({'message': sensor})

#* Funcion para obtener las estadisticas del sensor seleccionado
@app.route('/api/stats', methods=['GET'])
def Estadistics_Sensor():
    pass

#* Funcion para obtener los datos del sensor seleccionado
@app.route('/api/data', methods=['GET'])
def Data_Sensor():
    pass


# ------------------------- FUNCIONES ---------------------------

#* Funcion para encender el sensor de calidad de aire
def On_aire():
    pass

def Off_aire():
    pass

#* Funcion para encender el sensor de Temperatura
def On_Temperatura():
    pass

def Off_Temperatura():
    pass

#* Funcion para encender el sensor de Humedad
def On_Humedad():
    pass

def Off_Humedad():
    pass

#* Funcion para encender el sensor de Humedad
def On_Viento():
    pass

def Off_Viento():
    pass

#* Funcion para apagar el sensor de luminosidad
def Luminosidad_analogo(channel):
    
    global bus
    global PCF8591_ADDRESS

    
    if channel < 0 or channel > 3:
        return -1

    bus.write_byte(PCF8591_ADDRESS, 0x40 | channel)
    bus.read_byte(PCF8591_ADDRESS)  # leer una vez para iniciar la conversiï¿½n
    value = bus.read_byte(PCF8591_ADDRESS)
    return value


def On_luminosidad():
    global sensor_luminosidad
    sensor_luminosidad = True
    global datos    
    datos = []

    while sensor_luminosidad:
        analog_value = luminosidad_analogo(1)  # Leer desde el canal AO1
        print("Valor analogico leido desde AO1: ", analog_value)
        
        """
        # Interpretaciï¿½n de los valores
        if analog_value > 200:
            print("Muy oscuro")
        elif 150 < analog_value <= 200:
            print("Oscuridad baja")
        elif 100 < analog_value <= 150:
            print("Luz media")
        elif 50 < analog_value <= 100:
            print("Luz alta")
        else:
            print("Muy iluminado")
        
        """
        
        
        time.sleep(10)
        
        
def Off_luminosidad():
    global sensor_luminosidad
    global bus
    sensor_luminosidad = False
    bus.close()
    
#* Funcion para encender el sensor Barometrico

"""
#* Funcion para apagar el sensor de luminosidad
def Barometro_analogo(channel):
    
    global bus_Barometro
    global PCF8591_ADDRESS_Barometro

    
    if channel < 0 or channel > 3:
        return -1

    bus_Barometro.write_byte(PCF8591_ADDRESS_Barometro, 0x40 | channel)
    bus_Barometro.read_byte(PCF8591_ADDRESS_Barometro)  # leer una vez para iniciar la conversion
    value = bus_Barometro.read_byte(PCF8591_ADDRESS_Barometro)
    return value

def On_Presure_Barometric():
    global sensor_barometrico
    sensor_barometrico = True
    
    while sensor_barometrico:
        temperatura = bmp280.get_temperature()
        presion = bmp280.get_pressure()
         # Leer valor ADC del PCF8591 (Canal 0)
        adc_value = Barometro_analogo(0)

        # Formatear la temperatura y la presión
        format_temp = "{:.2f}".format(temperature)
        format_press = "{:.2f}".format(pressure)

        # Mostrar resultados
        degree_sign = u"\N{DEGREE SIGN}"
        print('Temperature = ' + format_temp + degree_sign + 'C')
        print('Pressure = ' + format_press + ' hPa')
        print(f'Analog Input (ADC Channel 0) = {adc_value}')

        # Esperar antes de la próxima lectura
        time.sleep(10)
        print(f'La temperatura es de: {temperatura}, la persion es de: {presion}')

#* Funcion para apagar el sensor Barometrico   


def Off_Presure_Barometric():
    global sensor_barometrico
    sensor_barometrico = False
    bus.close()


"""

#* El try es para manejar los errores que se puedan presentar en el servidor
try:
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000, debug=True)
except KeyboardInterrupt:
    print("\nLectura finalizada por el usuario.")
    sys.exit(0)
except ImportError:
    print("\nError de importación de librerias.")
    sys.exit(1)
except Exception as e:
    print(f"Se genero un Error: {e}")
    sys.exit(1)