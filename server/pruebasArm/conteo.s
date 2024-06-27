.section .data
fmt_float_add: .asciz "%.2f\n"

.global sum_array
sum_array:
    // Los primeros dos argumentos (el arreglo y su longitud) se pasan en los registros x0 y x1
    // Inicializar d0 (que usaremos para la suma) a 0
    mov x0, #0

// Crear un bucle que recorra el arreglo
suma_loop:
    // Si x1 (la longitud del arreglo) es 0, hemos terminado
    cbz x1, fin

    // Sumar el valor actual del arreglo a d0
    ldr s2, [x0], #4
    fadd d0, d0, s2

    // Decrementar x1 y continuar con el siguiente elemento
    sub x1, x1, #1
    b suma_loop

fin:
    // Dirección de la cadena de formato
    ldr x0, =fmt_float_add  
    // Mueve el resultado a w1 (utilizando la parte simple precisión de d0)       
    fmov w1, s0                    
    ret   