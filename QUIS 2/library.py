import numpy as np

# Definisikan matriks
A = np.array([[3, 0], [-1, 2], [1, 1]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

# Percobaan perkalian matrix A * C (diharapkan error)
try:
    result_A_C = np.dot(A, C)
    print("A * C =\n", result_A_C)
except ValueError as e:
    print("Error di A * C:", e)

# Percobaan perkalian matrix A * D (diharapkan error)
try:
    result_A_D = np.dot(A, D)
    print("A * D =\n", result_A_D)
except ValueError as e:
    print("Error di A * D:", e)

# Penjumlahan dan pengurangan matrix D dan E
D_plus_E = D + E
D_minus_E = D - E

print("D + E =\n", D_plus_E)
print("D - E =\n", D_minus_E)
