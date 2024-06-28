import ctypes
import os

# Load the shared library
lib_prmd = ctypes.CDLL(os.path.abspath("libprmedian.so"))

# Define the argument and return types for the function
lib_prmd.calculate_median.argtypes = (ctypes.POINTER(ctypes.c_float), ctypes.c_int)
lib_prmd.calculate_median.restype = ctypes.c_float

def calculate_median(numbers):
    # Convert Python list to C array
    arr = (ctypes.c_float * len(numbers))(*numbers)
    
    # Call the C function
    result = lib_prmd.calculate_median(arr, len(numbers))
    
    return result

# Test the function
numbers = [7.1, 15.2, 3.3, 110.4, 1.5, 220.6, 5.8, 2.9, 190.0]
median = calculate_median(numbers)
print(f"The median is: {median}")