
#* Los from son las librerias que vamos a utilizar en nuestro servidor pero solo algunas funciones de ellas
from flask      import Flask, request, jsonify
from flask_cors import CORS
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

sensor_barometrico = False

#* Funcion para encender el sensor seleccionado
@app.route('/api/on', methods=['POST'])
def On_Sensor():
    data = request.get_json()
    sensor = data.get('sensor')
    
    if sensor is None:
        return jsonify({'error': 'sensor and action are required'}), 400
    
    #* Aqui se debe de agregar la logica para encender el sensor
    if   sensor == '12':
        print("Sensor 12 encendido")
        On_Presure_Barometric()
    elif sensor == '13':
        print("Sensor 13 encendido")
    elif sensor == '14':
        print("Sensor 14 encendido")
    elif sensor == '15':
        print("Sensor 15 encendido")
    elif sensor == '16':
        print("Sensor 16 encendido")
    elif sensor == '17':
        print("Sensor 17 encendido")
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
        print("Sensor 12 apagado")
        Off_Presure_Barometric()
    elif sensor == '13':
        print("Sensor 13 apagado")
    elif sensor == '14':
        print("Sensor 14 apagado")
    elif sensor == '15':
        print("Sensor 15 apagado")
    elif sensor == '16':
        print("Sensor 16 apagado")
    elif sensor == '17':
        print("Sensor 17 apagado")
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

def On_Presure_Barometric():
    global sensor_barometrico
    sensor_barometrico = True
    
    bus = SMBus(1)
    bmp280 = BMP280(i2c_dev=bus)
    
    while sensor_barometrico:
        temperatura = bmp280.get_temperature()
        presion = bmp280.get_pressure()
        time.sleep(10)
        print(f'La temperatura es de: {temperatura}, 
              la persion es de: {presion}')
    
def Off_Presure_Barometric():
    global sensor_barometrico
    sensor_barometrico = False

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