
#* Los from son las librerias que vamos a utilizar en nuestro servidor pero solo algunas funciones de ellas
from flask      import Flask, request, jsonify
from flask_cors import CORS

import board
import busio

import adafruit_dht
from adafruit_bmp280 import Adafruit_BMP280_I2C

import smbus2

import ctypes
import os

#* Los imports son las librerias que vamos a utilizar en nuestro servidor pero todas las funciones de ellas
import sys
import time

#* creamos una instancia de la clase Flask
app = Flask(__name__)
#* creamos una instancia de la clase CORS
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


#------------------------- BLIBLIOTECA COMPARTIDA ---------------------------
lib = ctypes.CDLL(os.path.abspath("calculos.so"))


# ------------------------ DATOS --------------------------
datos = []
resultados = []

# ----------------------------VARIABLES ----------------------


#globales para sensor de calidad de aire

PCF8591_ADDRESS = 0x48
PCF8591_AO0 = 0x00

#globales para sensor de temperatura y humedad
sensor_temp = False

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
dht_device = None # Usa el pin GPIO4

#Sensor de velocidad viento
PIN_VIENTO = 22        #GPIO 25

#Sensor de luminosidad digital
PIN_LUZ = 13           #GPIO 17


# I2C
#Sensor de Calidad de aire I2C, velocidad viento y de Luminosidad I2C
PCF8591_ADDRESS = 0x48
bus = smbus2.SMBus(1)
bus_sensoraire = smbus2.SMBus(1)
bus_aire = smbus2.SMBus(1)
THRESHOLD = 128
counter = 0
last_value = None
start_time = time.time()

#Sensor de Presion Barometrica I2C
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = Adafruit_BMP280_I2C(i2c, address=0x76)
bmp280.sea_level_pressure = 1013.25  # Presion al nivel del mar en hPa



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
        On_Temp_Hum('temp')
    elif sensor == '13':
        print("Sensor Humedad encendido")
        On_Temp_Hum('hum')
    elif sensor == '14':
        print("Sensor Velocidad viento encendido")
        On_Viento()
    elif sensor == '15':
        print("Sensor Luminosidad encendido")
        On_luminosidad()
    elif sensor == '16':
        print("Sensor Calidad de aire encendido")
        On_aire()
    elif sensor == '17':
        print("Sensor Presion Barometrica encendido")
        On_Presure_Barometric()
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
        Off_Temp_Hum()
    elif sensor == '13':
        print("Sensor Humedad apagado")
        Off_Temp_Hum()
    elif sensor == '14':
        print("Sensor Velocidad viento apagado")
        Off_Viento()
    elif sensor == '15':
        print("Sensor Luminosidad apagado")
        Off_luminosidad()
    elif sensor == '16':
        print("Sensor Calidad de aire apagado")
        Off_aire()
    elif sensor == '17':
        print("Sensor Presion Barometrica apagado")
        Off_Presure_Barometric()
    else:
        return jsonify({'message': 'invalid sensor'}), 400
    
    return jsonify({'message': sensor})

#* Funcion para obtener las estadisticas del sensor seleccionado
@app.route('/api/stats', methods=['GET'])
def Estadistics_Sensor():
    # Aquí es donde obtendrías los datos del sensor en la vida real
    data = {
        "labels": ['Promedio', 'Mediana', 'DesviacionEstandar', 'Máximo', 'Mínimo', 'Moda'],
        "datasets": [
            {
                "label": 'Revenue',
                "backgroundColor": '#4e73df',
                "borderColor": '#4e73df',
                "data": [resultados[0], resultados[1], resultados[2], resultados[3], resultados[4], resultados[5]],
            },
        ],
    }
    return jsonify(data)

#* Funcion para obtener los datos del sensor seleccionado
@app.route('/api/data', methods=['GET'])
def Data_Sensor():
    # Aquí es donde obtendrías los datos del sensor en la vida real
    calculos_estadisticos()
    data = {
        "Promedio": resultados[0],
        "Mediana": resultados[1],
        "DesviacionEstandar": resultados[2],
        "Máximo": resultados[3],
        "Mínimo": resultados[4],
        "Moda": resultados[5]
    }
    return jsonify(data)


# ------------------------- FUNCIONES ---------------------------

#* Funcion para encender el sensor de calidad de aire
def On_aire():
    global sensor_aire
    sensor_aire = True
    while sensor_aire:
        ao0_value = read_ao0()
        # Convertir el valor le�do a voltaje (si es necesario)
        voltage = ao0_value / 255.0 * 3.3  # Si la alimentaci�n es de 3.3V
        print(f"AO0 Value: {ao0_value}, Voltage: {voltage:.2f}V")
        clasificacion(ao0_value)
        time.sleep(10)

    print("Leyendo datos de la calidad de aire de la zona...")

def clasificacion(analog_value):
    global datos
    datos = []
    # Convertir el valor anal�gico a una concentraci�n aproximada de CO2
    # Nota: Esta conversi�n es aproximada y depende de la calibraci�n espec�fica del sensor MQ-135
    # Aqu� asumimos que el valor anal�gico de 0 a 255 se mapea a una concentraci�n de CO2 en ppm
    co2_concentration = analog_value / 255.0 * 10000  # Ejemplo de mapeo: 0-255 a 0-10000 ppm

    # Clasificar la calidad del aire bas�ndose en la concentraci�n de CO2
    if co2_concentration < 1000:
        print("Buena")
        datos.append(1)

    else:
        print("Mala")
        datos.append(0)

def read_ao0():
    global PCF8591_ADDRESS
    global PCF8591_AO0
    # Leer el valor anal�gico del canal AO0
    bus.write_byte(PCF8591_ADDRESS, PCF8591_AO0)
    value = bus.read_byte(PCF8591_ADDRESS)  # Lectura dummy
    value = bus.read_byte(PCF8591_ADDRESS)
    return value


def Off_aire():
    global Switch_Sensoraire
    global bus_sensoraire
    Switch_Sensoraire = False
    bus_sensoraire.close()

    print("Sensor de calidad de aire apagado...")


#* Funcion para encender el sensor de Temperatura
def On_Temp_Hum(tipo_sensor):
    global sensor_temp
    global dht_device
    global datos


    dht_device = adafruit_dht.DHT11(board.D4)  # Usa el pin GPIO4
    datos = []
    sensor_temp = True
    # Intenta obtener una lectura del sensor
    while sensor_temp:
        try:
            # Intentar leer la temperatura y la humedad
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity

            # Imprimir los valores le�dos
            print(f"Temperatura: {temperature_c:.1f} �C")
            print(f"Humedad: {humidity:.1f} %")
            if tipo_sensor == 'temp':
                datos.append(temperature_c)
            else:
                datos.append(humidity)


        except RuntimeError as error:
            # Errores de lectura son comunes con los sensores DHT, simplemente intenta nuevamente
            print(f"Error al leer el sensor: {error.args[0]}")

        except Exception as error:
            dht_device.exit()
            raise error

        # Esperar antes de la pr�xima lectura
        time.sleep(10)


def Off_Temp_Hum():
    global sensor_temp
    sensor_temp = False



#* Funcion para encender el sensor de Viento


def read_analog(channel):
    if channel < 0 or channel > 3:
        raise ValueError("El canal debe estar entre 0 y 3")
    
    # Leer el valor anal�gico del canal seleccionado
    bus.write_byte(PCF8591_ADDRESS, channel)
    analog_value = bus.read_byte(PCF8591_ADDRESS)  # Leer el valor
    
    return analog_value


def On_Viento():
    sensor_viento = True
    global counter
    global last_value
    global start_time
    global THRESHOLD
    global datos
    datos= []
    last_value = read_analog(2)

    while sensor_viento:
        # Leer el valor del canal 0 (donde est� conectado el sensor)
        value = read_analog(2)
        
        # Detectar la transici�n de bajo a alto
        if last_value < THRESHOLD and value >= THRESHOLD:
            counter += 1
        
        # Actualizar el �ltimo valor le�do
        last_value = value
        
        # Calcular el tiempo transcurrido
        elapsed_time = time.time() - start_time
        
        if elapsed_time >= 1.0:
            # Calcular las RPM (ajustar seg�n el n�mero de ranuras del encoder)
            slots = 20  # N�mero de ranuras en el disco del encoder
            rpm = (counter / slots) / elapsed_time * 60
            
            # Imprimir las RPM
            print(f"Velocidad de rotaci�n: {rpm:.2f} RPM")
            
            # Reiniciar el contador y el tiempo
            counter = 0
            start_time = time.time()
            datos.append(rpm)
            time.sleep(10)



def Off_Viento():
    global sensor_viento
    global bus
    sensor_viento = False
    bus.close()

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
    datos.clear()

    while sensor_luminosidad:
        analog_value = Luminosidad_analogo(1)  # Leer desde el canal AO1
        print("Valor analogico leido desde AO1: ", analog_value)
        time.sleep(10)
        
        
def Off_luminosidad():
    global sensor_luminosidad
    global bus
    sensor_luminosidad = False
    bus.close()
    
#* Funcion para encender el sensor Barometrico


#* Funcion para apagar el sensor de luminosidad

def On_Presure_Barometric():
    global sensor_barometrico
    global datos
    sensor_barometrico = True
    datos.clear()

    
    while sensor_barometrico:
        # Leer datos del BMP280
        temperatura = bmp280.temperature
        presion = bmp280.pressure
        altitud = bmp280.altitude

        # Imprimir los valores le�dos
        print(f"Temperatura: {temperatura:.2f} C")
        print(f"Presion: {presion:.2f} hPa")
        print(f"Altitud: {altitud:.2f} m")
        
        # Agrega el valor de la presion a la lista
        datos.append(presion)

        # Esperar un segundo antes de la pr�xima lectura
        time.sleep(10)

#* Funcion para apagar el sensor Barometrico   


def Off_Presure_Barometric():
    global sensor_barometrico
    sensor_barometrico = False
    #bus.close()

#------------------------- CALCULOS ASM  ---------------------------

def calculos_estadisticos():
    global datos 
    global lib
    global resultados
    
    resultados = []
    
    #* Calculo para la Desviacion Estandar arm 64 bits
    # Cargar la libreria compartida
    lib = ctypes.CDLL('./Calculos/desEstandar/desEstandar.so')

    # Definir el prototipo de la funci�n
    lib.desEstandar.argtypes = (ctypes.POINTER(ctypes.c_float), ctypes.c_int)
    lib.desEstandar.restype = ctypes.c_float

    # Definir el arreglo de numeros
    num_elements = len(datos)

    # Convertir el arreglo a un tipo que ctypes pueda manejar
    ArrayType = ctypes.c_float * num_elements
    c_array = ArrayType(*datos)

    # Llamar a la funcion y obtener el resultado
    desEstandar = lib.desEstandar(c_array, num_elements)
    
    resultados.append(desEstandar)
    
    #*---------------------------------------------------------
    #* Calculo para la Mediana arm 64 bits
    # Cargar la libreria compartida
    lib = ctypes.CDLL('./Calculos/Mediana/mediana.so')
    
    # Definir el prototipo de la funcion
    lib.mediana.argtypes = (ctypes.POINTER(ctypes.c_float), ctypes.c_int)
    lib.mediana.restype = ctypes.c_float

    # Llamar a la funcion y obtener el resultado
    mediana = lib.mediana(c_array, num_elements)
    
    resultados.append(mediana)

    #Resultados de la calidad de aire
    cont1 = lib.conteo1(c_array, len(datos))
    cont0 = lib.conteo0(c_array, len(datos))
    

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