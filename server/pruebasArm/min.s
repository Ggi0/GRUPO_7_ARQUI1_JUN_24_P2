.global findMin

findMin:
        // x0 contiene la direcci�n del arreglo
        // x1 contiene el tama�o del arreglo
    ldr w2, [x0]  // Carga el primer elemento como m�nimo inicial
    mov x3, #1    // Inicializa el contador en 1

    loop:
        cmp x3, x1    // Compara el contador con el tama�o del arreglo
        b.ge end      // Si es mayor o igual, termina el loop
        ldr w4, [x0, x3, lsl #2]  // Carga el siguiente elemento
        cmp w4, w2    // Compara con el m�nimo actual
        b.ge next     // Si es mayor o igual, pasa al siguiente
        mov w2, w4    // Si es menor, actualiza el m�nimo

    next:
        add x3, x3, #1  // Incrementa el contador
        b loop          // Vuelve al inicio del loop

    end:
        mov x0, x2    // Mueve el resultado a x0 para devolverlo
        ret           // Retorna


/*
#2da version
.global findMin

findMin:
    // x0 contiene la dirección del arreglo
    // x1 contiene el tamaño del arreglo
    cbz x1, empty_array    // Si el tamaño es 0, maneja el caso especial

    ldr x2, [x0]           // Carga el primer elemento como mínimo inicial
    mov x3, #1             // Inicializa el contador en 1

loop:
    cmp x3, x1             // Compara el contador con el tamaño del arreglo
    b.ge end               // Si es mayor o igual, termina el loop
    ldr x4, [x0, x3, lsl #3]  // Carga el siguiente elemento (usando desplazamiento de 8 bytes)
    cmp x4, x2             // Compara con el mínimo actual
    csel x2, x4, x2, lt    // Selecciona el menor entre x4 y x2

    add x3, x3, #1         // Incrementa el contador
    b loop                 // Vuelve al inicio del loop

end:
    mov x0, x2             // Mueve el resultado a x0 para devolverlo
    ret                    // Retorna

empty_array:
    mov x0, #0             // Si el arreglo está vacío, devuelve 0
    ret

 */







/*
#3ra version

  .global findMin
findMin:
    // Prólogo de la función
    stp x29, x30, [sp, #-16]!  // Guarda el frame pointer y el link register
    mov x29, sp                // Establece el nuevo frame pointer

    // x0 contiene la dirección del arreglo
    // x1 contiene el tamaño del arreglo
    cbz x1, .Lempty_array      // Si el tamaño es 0, maneja el caso especial

    ldr x2, [x0]               // Carga el primer elemento como mínimo inicial
    mov x3, #1                 // Inicializa el contador en 1

.Lloop:
    cmp x3, x1                 // Compara el contador con el tamaño del arreglo
    b.ge .Lend                 // Si es mayor o igual, termina el loop
    ldr x4, [x0, x3, lsl #3]   // Carga el siguiente elemento (usando desplazamiento de 8 bytes)
    cmp x4, x2                 // Compara con el mínimo actual
    csel x2, x4, x2, lt        // Selecciona el menor entre x4 y x2
    add x3, x3, #1             // Incrementa el contador
    b .Lloop                   // Vuelve al inicio del loop

.Lend:
    mov x0, x2                 // Mueve el resultado a x0 para devolverlo
    b .Lreturn                 // Salta a la salida de la función

.Lempty_array:
    mov x0, #0                 // Si el arreglo está vacío, devuelve 0

.Lreturn:
    // Epílogo de la función
    ldp x29, x30, [sp], #16    // Restaura el frame pointer y el link register
    ret                        // Retorna de la función      

     */