.global findMin

.section .text

// findMin: Finds the minimum value in an array
// Inputs:
//   x0: Pointer to the array
//   x1: Length of the array
// Output:
//   x0: Minimum value
findMin:
    // Initialize x0 (result) with the first element of the array
    ldr w0, [x0]

    // Create a loop to compare each element
    loop:
        // If x1 (length) is 0, we're done
        cbz x1, done

        // Load the next element
        ldr w2, [x0], #4

        // Compare with the current minimum
        cmp w2, w0
        csel w0, w0, w2, lt  // Update minimum if w2 < w0

        // Decrement length and continue
        sub x1, x1, #1
        b loop

    done:
    ret
