from utils import read_system, multiply, print_matrix


def lu_decomposition(A):
    n = len(A)
    U = [row[:] for row in A]
    L = [[0.0 for j in range(n)] for i in range(n)]
    P = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    swaps = 0

    for k in range(n):
        p = k

        for i in range(k + 1, n):
            if abs(U[i][k]) > abs(U[p][k]):
                p = i

        if p != k:
            U[k], U[p] = U[p], U[k]
            P[k], P[p] = P[p], P[k]

            for j in range(k):
                L[k][j], L[p][j] = L[p][j], L[k][j]

            swaps += 1

        L[k][k] = 1.0

        for i in range(k + 1, n):
            c = U[i][k] / U[k][k]
            L[i][k] = c

            for j in range(k, n):
                U[i][j] -= c * U[k][j]

    return L, U, P, swaps


def solve_lu(L, U, P, b):
    n = len(b)
    pb = [0.0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            pb[i] += P[i][j] * b[j]

    z = [0.0 for i in range(n)]

    for i in range(n):
        val = pb[i]

        for j in range(i):
            val -= L[i][j] * z[j]

        z[i] = val / L[i][i]

    x = [0.0 for i in range(n)]

    for i in range(n - 1, -1, -1):
        val = z[i]

        for j in range(i + 1, n):
            val -= U[i][j] * x[j]

        x[i] = val / U[i][i]

    return x


def inverse_matrix(L, U, P):
    n = len(L)
    inv = [[0.0 for j in range(n)] for i in range(n)]

    for col in range(n):
        e = [0.0 for i in range(n)]
        e[col] = 1.0

        x = solve_lu(L, U, P, e)

        for row in range(n):
            inv[row][col] = x[row]

    return inv


A, b = read_system("lu.txt")
L, U, P, swaps = lu_decomposition(A)
x = solve_lu(L, U, P, b)

inv = inverse_matrix(L, U, P)
det = (-1) ** swaps
for i in range(len(A)):
    det *= U[i][i]

LU = multiply(L, U)
PA = multiply(P, A)
A_inv = multiply(A, inv)


print("Matrix L:")
print_matrix(L)

print("\nMatrix U:")
print_matrix(U)

print("\nL * U:")
print_matrix(LU)

print("\nSolution Ax = b:")
for i in range(len(x)):
    print(f"x{i + 1} = {x[i]:.6f}")

print("\nInverse matrix A^-1:")
print_matrix(inv)

print(f"\nDeterminant A: {det:.6f}")

print("\nA * A^-1:")
print_matrix(A_inv)

print("\nMatrix P:")
print_matrix(P)

print("\nP * A:")
print_matrix(PA)