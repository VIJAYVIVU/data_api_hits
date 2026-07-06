# ==========================================
# 1. INEFFICIENT LOOKUP IN A LIST (O(N^2))
# ==========================================
# Lookups in lists are slow. Checking elements in a loop creates quadratic time.
import time

large_list = list(range(10000))
search_items = list(range(5000, 15000))

start_time = time.time()
found_count = 0
for item in search_items:
    # Inefficient: Scanning the entire list from scratch every iteration
    if item in large_list:
        found_count += 1
print(f"List lookup took: {time.time() - start_time:.4f} seconds")


# ==========================================
# 2. REPETITIVE STRING CONCATENATION IN A LOOP
# ==========================================
# Strings are immutable. '+' creates a brand new string copy every single iteration.
words = ["python"] * 50000

start_time = time.time()
result_str = ""
for word in words:
    # Inefficient: Allocating new memory and copying the string over and over
    result_str += word + " "
print(f"String concatenation took: {time.time() - start_time:.4f} seconds")


# ==========================================
# 3. RE-EVALUATING FUNCTIONS IN LOOP CONDITIONS
# ==========================================
# The loop recalculates the same value on every single iteration instead of storing it.
data_list = list(range(20000))

start_time = time.time()
squared_values = []
for i in range(len(data_list)):
    # Inefficient: If this was a heavy function, calling it repeatedly kills speed
    # Also calculating len(data_list) inside loops unnecessarily is poor practice
    if i < len(data_list):
        squared_values.append(i ** 2)
print(f"Loop evaluation took: {time.time() - start_time:.4f} seconds")


# ==========================================
# 4. NESTED FOR-LOOPS FOR MATRIX MULTIPLICATION
# ==========================================
# Pure python loops are incredibly slow for mathematical operations on arrays.
size = 150
matrix_a = [[i for i in range(size)] for j in range(size)]
matrix_b = [[i for i in range(size)] for j in range(size)]
result_matrix = [[0 for i in range(size)] for j in range(size)]

start_time = time.time()
# Inefficient: Triple nested loops in native Python
for i in range(size):
    for j in range(size):
        for k in range(size):
            result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
print(f"Matrix multiplication took: {time.time() - start_time:.4f} seconds")


# ==========================================
# 5. UNNECESSARY DOT NOTATION LOOKUPS IN A LOOP
# ==========================================
# Python resolves object attributes during runtime. Looking them up inside a tight loop is slow.
import math

numbers = list(range(1000000))

start_time = time.time()
square_roots = []
for num in numbers:
    # Inefficient: Python resolves 'math.sqrt' attribute on every single loop iteration
    square_roots.append(math.sqrt(num))
print(f"Dot notation loop took: {time.time() - start_time:.4f} seconds")
