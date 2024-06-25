.global sum_array
sum_array:
    // Los primeros dos argumentos (el arreglo y su longitud) se pasan en los registros x0 y x1
    // Inicializar x2 (que usaremos para la suma) a 0
    fmov d2, #0.0

// Crear un bucle que recorra el arreglo
suma_loop:
    // Si x1 (la longitud del arreglo) es 0, hemos terminado
    cbz x1, media

    // Sumar el valor actual del arreglo a x2
    ldr s3, [x0], #4
    scvtf d3, s3
    fadd d2, d2, d3

    // Decrementar x1 y continuar con el siguiente elemento
    sub x1, x1, #1
    // Incrementa el contador de valores
    add x3, x3, #1
    b suma_loop

media:
    // Dividimos el valor total por la cantidad de elementos
    mov  x4, x3
    scvtf d4, x4
    fdiv d0, d2, d4

    // Mover el resultado (la suma) a x0 para devolverlo
    fmov x0, d0
    ret