import numpy as np
from utils import read_system

eps = 0.001


def simple_iteration(A, b, eps):
    n = len(A)
    x = [0.0 for i in range(n)]
    count = 0

    while True:
        new_x = [0.0 for i in range(n)]

        for i in range(n):
            s = 0.0
            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]

            new_x[i] = (b[i] - s) / A[i][i]

        diff = max(abs(new_x[i] - x[i]) for i in range(n))
        count += 1
        x = new_x

        if diff < eps:
            break

    return x, count


def seidel(A, b, eps):
    n = len(A)
    x = [0.0 for i in range(n)]
    count = 0

    while True:
        old_x = x[:]

        for i in range(n):
            s = 0.0

            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]

            x[i] = (b[i] - s) / A[i][i]

        diff = max(abs(x[i] - old_x[i]) for i in range(n))
        count += 1

        if diff < eps:
            break

    return x, count


A, b = read_system("iterations.txt")

x1, count1 = simple_iteration(A, b, eps)
x2, count2 = seidel(A, b, eps)
exact = np.linalg.solve(np.array(A), np.array(b))

print(f"Epsilon: {eps}")

print("\nSimple iteration method:")
for i in range(len(x1)):
    print(f"x{i + 1} = {x1[i]:.6f}")
print(f"Iterations: {count1}")

print("\nSeidel method:")
for i in range(len(x2)):
    print(f"x{i + 1} = {x2[i]:.6f}")
print(f"Iterations: {count2}")

print("\nReference solution:")
for i in range(len(exact)):
    print(f"x{i + 1} = {exact[i]:.6f}")

print("\nConvergence speed:")
if count1 < count2:
    print("Simple iteration method converges faster.")
elif count2 < count1:
    print("Seidel method converges faster.")
else:
    print("Both methods have the same number of iterations.")