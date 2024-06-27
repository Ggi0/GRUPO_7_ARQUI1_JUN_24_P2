.global contadorDatos

.section .text

// Cuenta la cantidad de datos en un arreglo de enteros
contadorDatos:
    // Argumentos:
    // x0 - dirección del arreglo

    // Inicializar x1 (contador) a 0
    mov x1, #0

    // Crear un bucle que recorra el arreglo
    loop:
        // Cargar el valor actual del arreglo en w2
        ldr w2, [x0], #4

        // Incrementar el contador (x1) independientemente del valor cargado
        add x1, x1, #1

        // Continuar con el siguiente elemento si no hemos llegado al final
        cbnz w2, loop

    // Mover el contador (la cantidad de elementos) a x0 para devolverlo
    mov x0, x1
    ret
