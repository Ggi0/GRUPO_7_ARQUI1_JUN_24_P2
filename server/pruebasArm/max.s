.global findMax

.section .text

// Encuentra el valor m�nimo en un arreglo de enteros
findMax:
    // Argumentos:
    // x0 - direcci�n del arreglo
    // x1 - longitud del arreglo

    // Si la longitud del arreglo es 0, devolver 0
    cbz x1, done

    // Inicializar x2 con el primer valor del arreglo (valor m�nimo inicial)
    ldr w2, [x0]

    // Ajustar x0 para que apunte al segundo elemento
    add x0, x0, #4
    sub x1, x1, #1

    // Crear un bucle que recorra el arreglo
    loop:
        // Si x1 (la longitud restante del arreglo) es 0, hemos terminado
        cbz x1, done

        // Cargar el valor actual del arreglo en w3
        ldr w3, [x0], #4

        // Comparar el valor actual con el m�nimo encontrado hasta ahora
        cmp w3, w2
        csel w2, w2, w3, lo  // w2 = (w2 < w3) ? w2 : w3

        // Decrementar x1 y continuar con el siguiente elemento
        sub x1, x1, #1
        b loop

    done:
    // Mover el resultado (el m�nimo) a x0 para devolverlo
    mov x0, x2
    ret
