import math
from utils import read_matrix, multiply, print_matrix

eps = 0.001


def jacobi(A, eps):
    n = len(A)
    A = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    while True:
        max_val = 0.0
        sum_sq = 0.0
        p = 0
        q = 1

        for i in range(n):
            for j in range(i + 1, n):
                sum_sq += A[i][j] ** 2

                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p = i
                    q = j

        if math.sqrt(sum_sq) < eps:
            break

        if A[p][p] == A[q][q]:
            phi = math.pi / 4
        else:
            phi = 0.5 * math.atan(2 * A[p][q] / (A[p][p] - A[q][q]))

        c = math.cos(phi)
        s = math.sin(phi)

        app = A[p][p]
        aqq = A[q][q]
        apq = A[p][q]

        A[p][p] = c * c * app + 2 * c * s * apq + s * s * aqq
        A[q][q] = s * s * app - 2 * c * s * apq + c * c * aqq
        A[p][q] = 0.0
        A[q][p] = 0.0

        for i in range(n):
            if i != p and i != q:
                aip = A[i][p]
                aiq = A[i][q]

                A[i][p] = c * aip + s * aiq
                A[p][i] = A[i][p]

                A[i][q] = -s * aip + c * aiq
                A[q][i] = A[i][q]

        for i in range(n):
            vip = V[i][p]
            viq = V[i][q]

            V[i][p] = c * vip + s * viq
            V[i][q] = -s * vip + c * viq

    vals = [A[i][i] for i in range(n)]

    return vals, V


A = read_matrix("jacobi.txt")

vals, V = jacobi(A, eps)

n = len(A)
Lambda = [[0.0 for j in range(n)] for i in range(n)]

for i in range(n):
    Lambda[i][i] = vals[i]

AV = multiply(A, V)
VL = multiply(V, Lambda)


print(f"Epsilon: {eps}")

print("\nEigenvalues:")
for i in range(n):
    print(f"lambda{i + 1} = {vals[i]:.6f}")

print("\nEigenvectors:")
for j in range(n):
    print(f"v{j + 1}:", end=" ")
    for i in range(n):
        print(f"{V[i][j]:.6f}", end=" ")
    print()

print("\nEigenvector matrix V:")
print_matrix(V)

print("\nA * V:")
print_matrix(AV)

print("\nV * Lambda:")
print_matrix(VL)