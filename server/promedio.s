.global _start

.section .data
filename: .asciz "input.txt"  // Nombre del archivo
buffer:   .space 100          // Buffer para leer el archivo
len:      .word 100           // Longitud m�xima del buffer
numbers:  .space 100          // Espacio para almacenar los n�meros convertidos

.section .text
_start:
    // Abrir el archivo
    MOV X0, #0                // stdin
    LDR X1, =filename         // Direcci�n del nombre del archivo
    MOV X2, #0                // O_RDONLY
    MOV X8, #56               // syscall: open
    SVC #0
    MOV X3, X0                // Guardar el descriptor de archivo en X3

    // Leer el archivo
    MOV X0, X3                // Descriptor de archivo
    LDR X1, =buffer           // Buffer donde se almacenar� el contenido
    LDR X2, =len              // Longitud m�xima a leer
    LDR W2, [X2]              // Longitud m�xima a leer (en W2)
    MOV X8, #63               // syscall: read
    SVC #0

    // Cerrar el archivo
    MOV X0, X3                // Descriptor de archivo
    MOV X8, #57               // syscall: close
    SVC #0

    // Convertir los caracteres le�dos a n�meros
    LDR X1, =buffer           // Direcci�n del buffer
    LDR X2, =numbers          // Direcci�n para almacenar los n�meros
    MOV X3, #0                // �ndice para almacenar en numbers

convert_loop:
    LDRB W4, [X1], #1         // Leer un byte del buffer
    CMP W4, #'0'              // Comparar con '0'
    BLT not_digit             // Si es menor que '0', no es un d�gito
    CMP W4, #'9'              // Comparar con '9'
    BGT not_digit             // Si es mayor que '9', no es un d�gito
    SUB W4, W4, #'0'          // Convertir car�cter a n�mero
    LDR W5, [X2, X3, LSL #2]  // Cargar el valor actual
    MUL W5, W5, W6           // Multiplicar por 10
    ADD W5, W5, W4            // A�adir el nuevo d�gito
    STR W5, [X2, X3, LSL #2]  // Almacenar el nuevo valor
    B convert_loop            // Repetir el bucle

not_digit:
    CMP W4, #','              // Comprobar si es una coma
    BNE end_of_input          // Si no es una coma, fin de la entrada
    ADD X3, X3, #1            // Incrementar el �ndice
    B convert_loop            // Repetir el bucle

end_of_input:
    // Sumar los numeros almacenados
    MOV X8, #93               // syscall: exit
    MOV X0, #0                // estado de salida
    SVC #0

