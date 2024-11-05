# Definisikan matriks sebagai nested lists
A = [[3, 0], [-1, 2], [1, 1]]
C = [[1, 4, 2], [3, 1, 5]]
D = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]

# Fungsi untuk perkalian matriks
def matrix_multiply(X, Y):
    # Cek jika dimensi kompatibel
    if len(X[0]) != len(Y):
        raise ValueError("Dimensi matriks tidak kompatibel untuk perkalian.")
    # Inisialisasi hasil
    result = [[0] * len(Y[0]) for _ in range(len(X))]
    # Proses perkalian
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Fungsi untuk penjumlahan matriks
def matrix_add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Fungsi untuk pengurangan matriks
def matrix_subtract(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Percobaan perkalian matrix A * C (diharapkan error)
try:
    result_A_C = matrix_multiply(A, C)
    print("A * C =\n", result_A_C)
except ValueError as e:
    print("Error di A * C:", e)

# Percobaan perkalian matrix A * D (diharapkan error)
try:
    result_A_D = matrix_multiply(A, D)
    print("A * D =\n", result_A_D)
except ValueError as e:
    print("Error di A * D:", e)

# Penjumlahan dan pengurangan matrix D dan E
D_plus_E = matrix_add(D, E)
D_minus_E = matrix_subtract(D, E)

print("D + E =\n", D_plus_E)
print("D - E =\n", D_minus_E)
