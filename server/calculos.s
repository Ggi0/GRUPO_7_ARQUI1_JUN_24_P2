.global sum_three
.global subtract_three
.global multiply_three

// Funcion de suma de tres numeros
sum_three:
    ADD x0, x0, x1  // Sumar el contenido de x0 y x1, y almacenar el resultado en x0
    ADD x0, x0, x2  // Sumar el contenido de x0 y x2, y almacenar el resultado en x0
    RET             // Retornar al llamador

// Funcion de resta de tres numeros
subtract_three:
    SUB x0, x0, x1  // Restar x1 de x0, y almacenar el resultado en x0
    SUB x0, x0, x2  // Restar x2 de x0, y almacenar el resultado en x0
    RET             // Retornar al llamador

// Funcion de multiplicacion de tres numeros
multiply_three:
    MUL x0, x0, x1  // Multiplicar el contenido de x0 y x1, y almacenar el resultado en x0
    MUL x0, x0, x2  // Multiplicar el contenido de x0 y x2, y almacenar el resultado en x0
    RET             // Retornar al llamador
