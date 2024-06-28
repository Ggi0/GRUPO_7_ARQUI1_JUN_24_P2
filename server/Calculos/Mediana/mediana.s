.global calculate_median

.data
a:                                      // No se define un tamaño estático aquí
b: .quad 0

.bss
c: .space 64

.text
calculate_median:
    // Guardar el frame pointer y el link register
    stp x29, x30, [sp, #-16]!
    mov x29, sp

    // Cargar dirección del arreglo y tamaño
    ldr x0, =a
    ldr x1, =b
    ldr x1, [x1]

    // Llamar a la función de ordenamiento
    bl func1

    // Calcular la mediana
    ldr x0, =a
    ldr x1, =b
    ldr x1, [x1]
    ldr x2, =c
    bl func2

    // Cargar el resultado en s0 (32 bits para float)
    ldr s0, [x2]

    // Convertir s0 a double en d0 para retorno
    scvtf d0, s0

    // Restaurar frame pointer y link register, y retornar
    ldp x29, x30, [sp], #16
    ret

// Función de ordenamiento (omitiendo detalles, similar a la anterior)
func1:

// Función para calcular la mediana con arreglo de tamaño dinámico
func2:
    tst x1, 1
    b.ne odd_case

    // Caso par
    mov x3, x1, lsr 1
    sub x4, x3, 1
    lsl x3, x3, 2
    lsl x4, x4, 2
    add x5, x0, x3
    add x6, x0, x4

    ldr s0, [x5]
    ldr s1, [x6]
    fadd s2, s0, s1
    fmov s3, 2.0
    fdiv s2, s2, s3

    b store_result

odd_case:
    // Caso impar (implementación no mostrada en detalle)

store_result:
    // Almacenar el resultado en c
    str s0, [x2]
    ret