.global sum_array

.section .text
sum_array:
    // Los primeros dos argumentos (el arreglo y su longitud) se pasan en los registros x0 y x1
    // Inicializar x2 (que usaremos para la suma) a 0
    mov x2, #0

    // Crear un bucle que recorra el arreglo
    loop:
        // Si x1 (la longitud del arreglo) es 0, hemos terminado
        cbz x1, done

        // Sumar el valor actual del arreglo a x2
        ldr w3, [x0], #4
        add x2, x2, w3, uxtw

        // Decrementar x1 y continuar con el siguiente elemento
        sub x1, x1, #1
        b loop

    done:
    // Mover el resultado (la suma) a x0 para devolverlo
    mov x0, x2
    ret