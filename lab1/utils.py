def read_system(fname):
    with open(fname, "r") as f:
        data = [[float(x) for x in line.split()] for line in f]

    A = [row[:-1] for row in data]
    b = [row[-1] for row in data]

    return A, b


def read_matrix(fname):
    with open(fname, "r") as f:
        return [[float(x) for x in line.split()] for line in f]


def multiply(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)

    res = [[0.0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                res[i][j] += A[i][k] * B[k][j]

    return res


def print_matrix(A):
    for row in A:
        for val in row:
            if abs(val) < 1e-10:
                val = 0.0
            print(f"{val:.6f}", end=" ")
        print()