.global sum_array
sum_array:
    // Los primeros dos argumentos (el arreglo y su longitud) se pasan en los registros x0 y x1
    // Inicializar d2 (que usaremos para la suma) a 0
    mov x2, #0

// Crear un bucle que recorra el arreglo
suma_loop:
    // Si x1 (la longitud del arreglo) es 0, hemos terminado
    cbz x1, media

    // Sumar el valor actual del arreglo a x2
    ldr w3, [x0], #4
    add x2, x2, w3

    // Decrementar x1 y continuar con el siguiente elemento
    sub x1, x1, #1
    // Incrementa el contador de valores
    add x3, x3, #1
    b suma_loop

media:
    // Convertir los operandos a flotante
    scvtf d2, x2
    scvtf d4, x3
    // Dividimos el valor total por la cantidad de elementos
    fdiv d0, d2, d4

    // Mover el resultado (la suma) a x0 para devolverlo
    fmov x0, d0
    ret