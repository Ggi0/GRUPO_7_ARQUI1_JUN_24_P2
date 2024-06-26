
#* Los from son las librerias que vamos a utilizar en nuestro servidor pero solo algunas funciones de ellas
from flask      import Flask, request, jsonify
from flask_cors import CORS

import board
import busio
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

sensor_aire = False
valor_sensoraire = 0
Switch_Sensoraire = False 



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
bus_sensoraire = smbus2.SMBus(1)


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
    elif sensor == '13':
        print("Sensor Humedad encendido")
    elif sensor == '14':
        print("Sensor Velocidad viento encendido")
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
    elif sensor == '13':
        print("Sensor Humedad apagado")
    elif sensor == '14':
        print("Sensor Velocidad viento apagado")
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
    pass

#* Funcion para obtener los datos del sensor seleccionado
@app.route('/api/data', methods=['GET'])
def Data_Sensor():
    pass


# ------------------------- FUNCIONES ---------------------------

#* Funcion para encender el sensor de calidad de aire
def On_aire():
    global sensor_aire
    sensor_aire = True

    print("Leyendo datos de la calidad de aire de la zona...")
    Datos_sensoraire()

def leerADC(canal):
    global bus_sensoraire
    global PCF8591_ADDRESS
    global valor_sensoraire

    bus_sensoraire.write_byte(PCF8591_ADDRESS, canal)
    valor_sensoraire = bus_sensoraire.read_byte(PCF8591_ADDRESS)
    return valor_sensoraire


def Clasificar_Calidad(aireVoltaje):
    if aireVoltaje < 1.5:
        return "Calidad de Aire Buena..."
    else:
        return "Calidad de Aire Mala..."

def Datos_sensoraire():
    global valor_sensoraire
    global Switch_Sensoraire
    Switch_Sensoraire = True

    global datos    
    datos = []

    while Switch_Sensoraire:
        Valor_adc = leerADC(0x40)
        # El voltaje es el valor que se tomara para el arm
        Voltage = Valor_adc / 255.0 * 3.3
        print(f"Voltaje obtenido: {Voltage: .2f} V")
        datos.append(Voltage)
        # Clasifica la calidad del aire de la zona
        sesgo = Clasificar_Calidad(Voltage)
        print(sesgo)
        time.sleep(10)
        
    print("Sensor de calidad de aire desactivado...")
    

def Off_aire():
    global Switch_Sensoraire
    global bus_sensoraire
    Switch_Sensoraire = False
    bus_sensoraire.close()

    print("Sensor de calidad de aire apagado...")


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
    datos.clear()

    while sensor_luminosidad:
        analog_value = Luminosidad_analogo(1)  # Leer desde el canal AO1
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
    
    c_array = (ctypes.c_int * len(datos))(*datos)
    
    result_suma = lib.sum_array(c_array, len(datos))
    print(f"La suma de los valores es: {result_suma}")
    resultados.append(result_suma)
    
    



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