import math
import cmath
import numpy as np
from utils import read_matrix, multiply, print_matrix

eps = 0.001


def qr_decomposition(A):
    n = len(A)
    R = [row[:] for row in A]
    Q = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for k in range(n - 1):
        b = [R[i][k] for i in range(k, n)]

        norm = math.sqrt(sum(val ** 2 for val in b))
        sign = 1 if b[0] >= 0 else -1

        v = [0.0 for i in range(n)]

        for i in range(len(b)):
            v[k + i] = b[i]

        v[k] += sign * norm

        vtv = sum(val ** 2 for val in v)

        H = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                H[i][j] -= 2 * v[i] * v[j] / vtv

        R = multiply(H, R)
        Q = multiply(Q, H)

    return Q, R


def block_values(A, i):
    a = A[i][i]
    b = A[i][i + 1]
    c = A[i + 1][i]
    d = A[i + 1][i + 1]

    D = (a + d) ** 2 - 4 * (a * d - b * c)

    l1 = ((a + d) + cmath.sqrt(D)) / 2
    l2 = ((a + d) - cmath.sqrt(D)) / 2

    return l1, l2


def qr_eigenvalues(A, eps):
    n = len(A)
    Ak = [row[:] for row in A]
    old_vals = None

    while True:
        Q, R = qr_decomposition(Ak)
        Ak = multiply(R, Q)

        vals = []
        i = 0
        ready = True

        while i < n:
            s = math.sqrt(sum(Ak[j][i] ** 2 for j in range(i + 1, n)))

            if s < eps:
                vals.append(complex(Ak[i][i]))
                i += 1
            elif i + 1 < n:
                l1, l2 = block_values(Ak, i)
                vals.append(l1)
                vals.append(l2)
                i += 2

        if old_vals is None:
            ready = False
        else:
            for i in range(n):
                if abs(vals[i] - old_vals[i]) > eps:
                    ready = False
                    break

        if ready:
            return vals

        old_vals = vals


A = read_matrix("qr.txt")
Q, R = qr_decomposition(A)
QR = multiply(Q, R)
vals = qr_eigenvalues(A, eps)

print("Matrix A:")
print_matrix(A)

print("\nMatrix Q:")
print_matrix(Q)

print("\nMatrix R:")
print_matrix(R)

print("\nQ * R:")
print_matrix(QR)

print("\nEigenvalues:")
for i in range(len(vals)):
    val = vals[i]

    if abs(val.imag) < eps:
        print(f"lambda{i + 1} = {val.real:.6f}")
    else:
        print(f"lambda{i + 1} = {val.real:.6f} {val.imag:+.6f}i")


complex_A = [[1, -2, 0], [2, 1, 0], [0, 0, 3]]
complex_vals = np.linalg.eigvals(np.array(complex_A))

print("\nMatrix with complex conjugate eigenvalues:")
print_matrix(complex_A)

print("\nComplex eigenvalues (NumPy check):")
for val in complex_vals:
    print(val)