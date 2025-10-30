# code-optimizer-and-common-for-subexpressions

📘 Overview

This project implements a code optimizer that detects and eliminates common subexpressions in intermediate code.
The goal is to improve efficiency by avoiding redundant computations and reducing execution time.
       
#Example Input

t1 = a + b
t2 = t1 * c
t3 = a + b
t4 = t3 * d

#Sample Output

t1 = a + b
t2 = t1 * c
t4 = t1 * d
