import ctypes
import os

# Cargar la biblioteca compartida
lib = ctypes.CDLL(os.path.abspath("barometro.so"))

# Crear un arreglo en Python
py_array = [6,2,3,2]

# Convertir el arreglo de Python a un arreglo de C
c_array = (ctypes.c_int * len(py_array))(*py_array)

def main():
    
    # Declarar los tipos de retorno y argumentos de las funciones ensamblador
    lib.sum_array.restype = ctypes.c_float
    result = lib.sum_array(c_array, len(py_array))
    print(f"Resultado de la suma: {result}")

if __name__ == "__main__":
    main()