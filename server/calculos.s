.global sum
.global subtract
.global multiply

// Funcion de suma
sum:
    ADD r0, r0, r1  // Sumar el contenido de r0 y r1, y almacenar el resultado en r0
    BX lr           // Retornar al llamador

// Funcion de resta
subtract:
    SUB r0, r0, r1  // Restar r1 de r0, y almacenar el resultado en r0
    BX lr           // Retornar al llamador

// Funcion de multiplicacion
multiply:
    MUL r0, r0, r1  // Multiplicar el contenido de r0 y r1, y almacenar el resultado en r0
    BX lr           // Retornar al llamador
