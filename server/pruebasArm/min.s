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