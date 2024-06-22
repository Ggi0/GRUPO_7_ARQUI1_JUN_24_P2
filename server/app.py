from flask import Flask, request, jsonify
from flask_cors import CORS
#import RPi.GPIO as GPIO
import sys
import time
import threading




app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# ----------------------------VARIABLES ----------------------


'''
# Tipo de configuracion de los puertos
GPIO.setmode(GPIO.BOARD)

# Desactivamos alertas de GPIO
GPIO.setwarnings(False)

'''


# ------------------------- DECLARACION DE PUERTOS---------------------------


#Temperatura

TEMP = 11


#Humedad

HUMEDAD = 13

'''
# LED verde es el pin 29 con GPIO 5
# LED Roja es el pin 16 con GPIo 23
PIN_IN1_STEPPER = 31
PIN_IN2_STEPPER = 33
PIN_IN3_STEPPER = 35
PIN_IN4_STEPPER = 37
PIN_IN5_LEDGREEN = 29
PIN_IN6_LEDRED = 16

#LUCES CUARTOS
PIN_A = 18
PIN_B = 22
PIN_C = 23

#SERVOMOTOR
PIN_SERVO = 12

# LASER 

PIN_LASER = 38 #GPIO20

# fotoresistencia
PIN_F1 = 11 # GPIO17 
PIN_F2 = 21 # GPIO19

# buzzer
PIN_BUZZER = 40 #GPIO21

# Luz externa
PIN_LEDf = 36 #GPIO16


# ---- Sensor yair ------
# Configurar los pines GPIO para los bits binarios
bit0 = 8  # Pin 11 en la Raspberry Pi GPIO 14
bit1 = 32 # Pin 12 en la Raspberry Pi GPIO 12
bit2 = 7   # Pin 13 en la Raspberry Pi GPIO 4
bit3 = 10  # Pin 15 en la Raspberry Pi GPIO 15


# Configurar los pines GPIO para el sensor ultras�nico
TRIG = 13  # Pin 16 en la Raspberry Pi GPIO 27
ECHO = 15  # Pin 18 en la Raspberry�Pi�GPIO�22


'''


# ------------------ CONFIGURACIONES ----------------------


# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 5/float(1000)

# Control de los hilos
running = False
pause = threading.Event()
pause.set()
iniciar_stepper = True

# Control creacion de api
crear = True

#-------------------------FUNCIONES TEMPERATURA --------------------------

def temperatura():
    pass





#--------------------------FUNCIONES HUMEDAD-----------------------------


def Humedad():
    pass
        
    
 
    

#---------------------FUNCIONES VELOCIDAD VIENTO--------------------------
def Vel_viento():
    pass
    



'''

def start_motor():
    global running
    if not running:
        running = True
        threading.Thread(target=activar_motor_stepper, daemon=True).start()
        print("Motor iniciado")

'''

#---------------------FUNCIONES LUMINOSIDAD-----------------------------
def Luminosidad():
    pass

#---------------------FUNCIONES CALIDAD DE AIRE-------------------------
def Calidad_Aire():
    pass

#---------------------FUNCIONES PRESION BAROMETRICA-----------------------
def Presion_barometrica():
    pass

    


#TEMPERATURA 
@app.route('/api/activarTemp', methods=['POST'])
def activar_Temp():

    data = request.json
    estado = data.get('estado')

    if not isinstance(estado, int):
        return jsonify({"error": "Los parámetros 'cuarto' y 'estado' deben ser numéricos"}), 400

    
    return jsonify({"mensaje": "Estado del LED actualizado correctamente"}), 200

@app.route('/api/datosTemp', methods=['GET'])
def datos_Temp():
    
    Temp = request.args.get('cuarto', type=int)

    if Temp is None:
        return jsonify({"error": "El parámetro 'cuarto' es necesario y debe ser numérico"}), 400

 
    return jsonify({"Datos": Temp}), 200
    
  

#HUMEDAD
@app.route('/api/activarHum', methods=['POST'])
def activar_Hum():

    data = request.json
    estado = data.get('estado')

    if not isinstance(estado, int):
        return jsonify({"error": "Los parámetros 'cuarto' y 'estado' deben ser numéricos"}), 400

    
    return jsonify({"mensaje": "Estado del LED actualizado correctamente"}), 200

@app.route('/api/datosHum', methods=['GET'])
def datos_Hum():
    
    Temp = request.args.get('cuarto', type=int)

    if Temp is None:
        return jsonify({"error": "El parámetro 'cuarto' es necesario y debe ser numérico"}), 400

 
    return jsonify({"Datos": Temp}), 200

#VELOCIDAD VIENTO
@app.route('/api/activarViento', methods=['POST'])
def activar_Viento():

    data = request.json
    estado = data.get('estado')

    if not isinstance(estado, int):
        return jsonify({"error": "Los parámetros 'cuarto' y 'estado' deben ser numéricos"}), 400

    
    return jsonify({"mensaje": "Estado del LED actualizado correctamente"}), 200

@app.route('/api/datosViento', methods=['GET'])
def datos_Viento():
    
    Temp = request.args.get('cuarto', type=int)

    if Temp is None:
        return jsonify({"error": "El parámetro 'cuarto' es necesario y debe ser numérico"}), 400

 
    return jsonify({"Datos": Temp}), 200

    
#LUMINOSIDAD


@app.route('/api/activarLuminosidad', methods=['POST'])
def activar_Luminosidad():

    data = request.json
    estado = data.get('estado')

    if not isinstance(estado, int):
        return jsonify({"error": "Los parámetros 'cuarto' y 'estado' deben ser numéricos"}), 400

    
    return jsonify({"mensaje": "Estado del LED actualizado correctamente"}), 200

@app.route('/api/datosLuminosidad', methods=['GET'])
def datos_Luminosidad():
    
    Temp = request.args.get('cuarto', type=int)

    if Temp is None:
        return jsonify({"error": "El parámetro 'cuarto' es necesario y debe ser numérico"}), 400

 
    return jsonify({"Datos": Temp}), 200

#CALIDAD DE AIRE

@app.route('/api/activarAire', methods=['POST'])
def activar_Aire():

    data = request.json
    estado = data.get('estado')

    if not isinstance(estado, int):
        return jsonify({"error": "Los parámetros 'cuarto' y 'estado' deben ser numéricos"}), 400

    
    return jsonify({"mensaje": "Estado del LED actualizado correctamente"}), 200

@app.route('/api/datosAire', methods=['GET'])
def datos_Aire():
    
    Temp = request.args.get('cuarto', type=int)

    if Temp is None:
        return jsonify({"error": "El parámetro 'cuarto' es necesario y debe ser numérico"}), 400

 
    return jsonify({"Datos": Temp}), 200

# PRESION BAROMETRICA

@app.route('/api/activarPresion', methods=['POST'])
def activar_Presion():

    data = request.json
    estado = data.get('estado')

    if not isinstance(estado, int):
        return jsonify({"error": "Los parámetros 'cuarto' y 'estado' deben ser numéricos"}), 400

    
    return jsonify({"mensaje": "Estado del LED actualizado correctamente"}), 200

@app.route('/api/datosPresion', methods=['GET'])
def datos_Presion():
    
    Temp = request.args.get('cuarto', type=int)

    if Temp is None:
        return jsonify({"error": "El parámetro 'cuarto' es necesario y debe ser numérico"}), 400

 
    return jsonify({"Datos": Temp}), 200


#Codigo que se ejecuta solo una vez
def setup():
    #Declaracion de GPIO input o output
    #GPIO.setup(LED1, GPIO.OUT)
    
    '''
    
    # ---- MOTORES ----
    GPIO.setup(MOTOR, GPIO.OUT)

    # LEDS DEL MOTOR STEPPER
    GPIO.setup(PIN_IN5_LEDGREEN, GPIO.OUT)
    GPIO.setup(PIN_IN6_LEDRED, GPIO.OUT)
    
    #MOTOR STEPPER
    GPIO.setup(PIN_IN1_STEPPER,GPIO.OUT)
    GPIO.setup(PIN_IN2_STEPPER,GPIO.OUT)
    GPIO.setup(PIN_IN3_STEPPER,GPIO.OUT)
    GPIO.setup(PIN_IN4_STEPPER,GPIO.OUT)

    # ---- LUCES CUARTOS ----
    GPIO.setup(PIN_A, GPIO.OUT)
    GPIO.setup(PIN_B, GPIO.OUT)
    GPIO.setup(PIN_C, GPIO.OUT)

    # ---- SERVOMOTOR ----
    GPIO.setup(PIN_SERVO, GPIO.OUT)
    
     # ---- LASER ----
    GPIO.setup(PIN_LASER, GPIO.OUT)
    GPIO.setup(PIN_LEDf, GPIO.OUT)
    GPIO.setup(PIN_BUZZER, GPIO.OUT)
    GPIO.setup(PIN_F1, GPIO.IN)
    GPIO.setup(PIN_F2, GPIO.IN)


    # ---- LASER ----
    GPIO.setup(PIN_LASER, GPIO.OUT)
    GPIO.setup(PIN_LEDf, GPIO.OUT)
    GPIO.setup(PIN_BUZZER, GPIO.OUT)
    GPIO.setup(PIN_F1, GPIO.IN)
    GPIO.setup(PIN_F2, GPIO.IN)
    
    # --- PANTALLA LCD ---
    # Mostrar mensaje de bienvenida durante 10 segundos
    
    global lcd
    pantalla = mostrar_bienvenida(lcd)
    
    
    # ----- Iniciar apagados los puertos -------
    #GPIO.output(LED1, 0)
    GPIO.output(MOTOR, 0)
    #Iniciar apagados los puertos
    GPIO.output(PIN_IN1_STEPPER,0)
    GPIO.output(PIN_IN2_STEPPER,0)
    GPIO.output(PIN_IN3_STEPPER,0)
    GPIO.output(PIN_IN4_STEPPER,0)
    GPIO.output(PIN_IN5_LEDGREEN,0)
    GPIO.output(PIN_IN6_LEDRED, 1)

    # ----- Sensor YAIR  set mode y output------

    # Inicializar el pin TRIG en bajo
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(2)  
    
    '''
    

 
try:

    
    while True:
        time.sleep(1)  # Mantener el hilo principal dormido

        if crear == True:
            if __name__ == '__main__':
                setup()
                
                crear = False
                app.run(host='0.0.0.0', port=8000, debug=True, use_reloader=False)
        
except KeyboardInterrupt:
        running = False
        #GPIO.cleanup()