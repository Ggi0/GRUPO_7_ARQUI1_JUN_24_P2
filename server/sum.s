.global _start

.section .data
num1: .word 10
num2: .word 20
sum:  .word 0

.section .text
_start:
    LDR X0, =num1
    LDR W1, [X0]     // Cargar num1 en W1
    LDR X0, =num2
    LDR W2, [X0]     // Cargar num2 en W2
    ADD W3, W1, W2   // W3 = W1 + W2
    LDR X0, =sum
    STR W3, [X0]     // Guardar W3 en sum

    MOV X8, #93      // syscall: exit
    MOV X0, #0       // estado de salida
    SVC #0           // llamada al sistema
