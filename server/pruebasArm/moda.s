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



/*
.global moda

.section .text

// Encuentra la moda (valor más frecuente) en un arreglo de enteros de 64 bits
moda:
    // Argumentos:
    // x0 - dirección del arreglo
    // x1 - longitud del arreglo

    // Si la longitud del arreglo es 0, devolver 0
    cbz x1, done

    // Variables locales
    mov x2, #0       // Valor actual
    mov x3, #0       // Moda actual
    mov x4, #0       // Frecuencia del valor actual
    mov x5, #0       // Frecuencia máxima encontrada
    mov x6, x1       // Copia de la longitud del arreglo

    // Cargar el primer valor
    ldr x2, [x0], #8

    // Crear un bucle que recorra el arreglo
loop:
    // Decrementar el contador
    sub x6, x6, #1
    cbz x6, check_last

    // Cargar el siguiente valor del arreglo en x7
    ldr x7, [x0], #8

    // Si el valor actual es igual al valor anterior
    cmp x2, x7
    beq increment_frequency

    // Si son diferentes, actualizar contadores
    b update_count

increment_frequency:
    // Incrementar la frecuencia del valor actual
    add x4, x4, #1
    b continue_loop

update_count:
    // Si la frecuencia del valor actual es mayor que la frecuencia máxima encontrada hasta ahora
    cmp x4, x5
    blt no_update_moda
    mov x3, x2       // Actualizar la moda
    mov x5, x4       // Actualizar la frecuencia máxima

no_update_moda:
    mov x2, x7       // Actualizar el valor actual
    mov x4, #1       // Reiniciar la frecuencia del nuevo valor

continue_loop:
    // Continuar con el siguiente elemento
    cbnz x6, loop

check_last:
    // Comprobar si el último valor tiene la frecuencia más alta
    add x4, x4, #1
    cmp x4, x5
    csel x3, x2, x3, gt

done:
    // Devolver la moda en x0
    mov x0, x3
    ret



 */


 /*
 // version 3

 .global moda

moda:
    // Prólogo de la función
    stp x29, x30, [sp, #-16]!
    mov x29, sp

    // x0 - dirección del arreglo
    // x1 - longitud del arreglo

    cbz x1, .Lempty_array

    mov x2, #0       // Valor actual
    mov x3, #0       // Moda actual
    mov x4, #0       // Frecuencia del valor actual
    mov x5, #0       // Frecuencia máxima encontrada
    mov x6, x1       // Copia de la longitud del arreglo

    ldr x2, [x0], #8  // Cargar el primer valor

.Lloop:
    sub x6, x6, #1
    cbz x6, .Lcheck_last

    ldr x7, [x0], #8  // Cargar el siguiente valor

    cmp x2, x7
    beq .Lincrement_frequency

    // Si son diferentes, actualizar contadores
    cmp x4, x5
    b.le .Lno_update_moda
    mov x3, x2
    mov x5, x4

.Lno_update_moda:
    mov x2, x7
    mov x4, #1
    b .Lcontinue_loop

.Lincrement_frequency:
    add x4, x4, #1

.Lcontinue_loop:
    cbnz x6, .Lloop

.Lcheck_last:
    add x4, x4, #1
    cmp x4, x5
    csel x3, x2, x3, gt

.Lempty_array:
    mov x0, x3  // Devolver la moda (o 0 si el arreglo está vacío)

    // Epílogo de la función
    ldp x29, x30, [sp], #16
    ret
 
  */