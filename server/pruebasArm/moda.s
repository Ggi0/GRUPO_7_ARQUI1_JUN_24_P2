.global moda

.section .text

// Encuentra la moda (valor más frecuente) en un arreglo de enteros
moda:
    // Argumentos:
    // x0 - dirección del arreglo
    // x1 - longitud del arreglo

    // Si la longitud del arreglo es 0, devolver 0 (o un valor indicativo de que no hay moda)
    cbz x1, done

    // Variables locales
    mov x2, #0       // Valor actual
    mov x3, #0       // Moda actual
    mov x4, #0       // Frecuencia del valor actual
    mov x5, #0       // Frecuencia máxima encontrada

    // Crear un bucle que recorra el arreglo
    loop:
        // Cargar el valor actual del arreglo en w2
        ldr w2, [x0], #4

        // Si el valor actual es diferente al valor anterior
        cmp x2, w2
        bne update_count

        // Incrementar la frecuencia del valor actual
        add x4, x4, #1
        b continue_loop

    update_count:
        // Si la frecuencia del valor actual es mayor que la frecuencia máxima encontrada hasta ahora
        cmp x4, x5
        csel x3, x3, x2, gt  // Actualizar la moda si la frecuencia actual es mayor
        mov x5, x4           // Actualizar la frecuencia máxima
        mov x2, w2           // Actualizar el valor actual
        mov x4, #1           // Reiniciar la frecuencia del nuevo valor

    continue_loop:
        // Decrementar x1 y continuar con el siguiente elemento
        sub x1, x1, #1
        cbnz x1, loop

    done:
    // Si hemos terminado y el último valor tiene la frecuencia más alta, actualizar la moda
    csel x0, x3, x2, gt
    ret
