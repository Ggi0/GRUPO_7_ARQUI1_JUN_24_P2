.global sum_array
sum_array:
    // Los primeros dos argumentos (el arreglo y su longitud) se pasan en los registros x0 y x1
    // Inicializar x2 (que usaremos para la suma) a 0
    mov x2, #0

// Crear un bucle que recorra el arreglo
suma_loop:
    // Si x1 (la longitud del arreglo) es 0, hemos terminado
    cbz x1, media

    // Sumar el valor actual del arreglo a x2
    ldr s3, [x0], #4
    fadd d2, d2, s3

    // Decrementar x1 y continuar con el siguiente elemento
    sub x1, x1, #1
    // Incrementa el contador de valores
    add x3, x3, #1
    b suma_loop

media:
    // Dividimos el valor total por la cantidad de elementos
    mov  x4, x3
    fdiv d0, d2, x3

total_loop:
    // Si x1 (la longitud del arreglo) es 0, hemos terminado
    cbz x4, divide

    // Sumar el valor actual del arreglo a x2
    ldr s4, [x0], #4
    // resta los valores en absoluto
    fsub d4, d0, s4
    // Obtiene el valor absoluto
    fabs d4, d4
    // hace la operacion de potencia
    fmul d5, d4, d4

    // suma los valores de potencia
    fadd d6, d6, d5 
    // Decrementar x1 y continuar con el siguiente elemento
    sub x4, x4, #1
    // Incrementa el contador de valores
    add x5, x5, #1
    b total_loop

divide:
    // divimos el valor
    ldr s5, [x5]
    fdiv d7, d6, s5

    // generamos raiz
    //Calcular la raiz cuadrada del registro d0
    fsqrt d1, d7

    // Mover el resultado (la suma) a x0 para devolverlo
    mov x0, d1
    ret