.global sum_array

sum_array:
// x0 = puntero al arreglo, x1 = n?mero de elementos
    mov w2, #0                // Inicializar el ?ndice
    fmov s0, wzr              // Inicializar la suma a 0.0

loop:
    ldr s1, [x0, x2, lsl #2]  // Cargar el siguiente valor del arreglo en s1
    fadd s2, s2, s1           // s0 += s1
    add x2, x2, #1            // Incrementar el ?ndice
    cmp x2, x1                // Comparar el ?ndice con el n?mero de elementos
    b.lt loop                 // Si el ?ndice es menor, repetir el bucle

    // Convertir x1 (n?mero de elementos) a flotante en s1
    ucvtf s1, x1              // s1 = (float)x1
    fdiv s2, s2, s1           // s0 /= s1

    // Calcular la suma de los cuadrados de las diferencias
   mov w2, #0        // Reiniciar el índice

loop_square:
   ldr s3, [x0, x2, lsl #2]  // Cargar el siguiente valor del arreglo en s5
   fsub s4, s3, s2           // s4 = s3 - s0
   //fabs s4, s4               // Valor absoluto de s4
   //fmul s5, s4, s4           // s4 = s4 * s4 (elevar al cuadrado)
   fadd s0, s0, s4           // Sumar al acumulador de cuadrados
   add x2, x2, #1            // Incrementar el índice
   cmp x2, x1                // Comparar el índice con el número de elementos
   b.lt loop_square          // Si el índice es menor, repetir el bucle de cuadrados

   ret                       // Retornar el resultado en s0                