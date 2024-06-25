import ctypes
import os

# Cargar la biblioteca compartida
lib = ctypes.CDLL(os.path.abspath("liboperations.so"))

# Declarar los tipos de retorno y argumentos de las funciones ensamblador
lib.sum.restype = ctypes.c_int
lib.sum.argtypes = [ctypes.c_int, ctypes.c_int]

lib.subtract.restype = ctypes.c_int
lib.subtract.argtypes = [ctypes.c_int, ctypes.c_int]

lib.multiply.restype = ctypes.c_int
lib.multiply.argtypes = [ctypes.c_int, ctypes.c_int]

def main():
    while True:
        print("Seleccione la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. Salir")

        choice = input("Ingrese su elección (1/2/3/4): ")

        if choice == '4':
            print("Saliendo...")
            break

        if choice not in ['1', '2', '3']:
            print("Opción inválida. Intente de nuevo.")
            continue

        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue

        if choice == '1':
            result = lib.sum(num1, num2)
            print(f"Resultado de la suma: {result}")
        elif choice == '2':
            result = lib.subtract(num1, num2)
            print(f"Resultado de la resta: {result}")
        elif choice == '3':
            result = lib.multiply(num1, num2)
            print(f"Resultado de la multiplicación: {result}")

if __name__ == "__main__":
    main()
