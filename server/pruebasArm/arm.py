import ctypes
import os

# Cargar la biblioteca compartida
#lib = ctypes.CDLL(os.path.abspath("barometro.so"))
#lib2 = ctypes.CDLL(os.path.abspath("max.so"))
lib3 = ctypes.CDLL(os.path.abspath("min.so"))
lib4 = ctypes.CDLL(os.path.abspath("contadorDatos.so"))
lib5 = ctypes.CDLL(os.path.abspath("moda.so"))

# Crear un arreglo en Python
py_array = [10, 3, 90, 57, 91, 2, 1, 7]

# Convertir el arreglo de Python a un arreglo de C
c_array = (ctypes.c_int * len(py_array))(*py_array)

def main():
    
    # Declarar los tipos de retorno y argumentos de las funciones ensamblador

    #result = lib.sum_array(c_array, len(py_array))
    #print(f"Resultado de la suma: {result}")
      
    #result_Max = lib2.findMax(c_array, len(py_array))
    #print(f"Resultado Max del array: {result_Max}")
    
    result_min = lib3.findMin(c_array, len(py_array))
    print(f"Resultado Min del array: {result_min}")
    
    result_contador = lib4.contadorDatos(c_array)
    print(f"Resultado Datos del array: {result_contador}")
    
    result_moda = lib5.moda(c_array, len(py_array))
    print(f"Resultado moda del array: {result_moda}")
    

if __name__ == "__main__":
    main()
    