import math


def f1(x1, x2):
    return x1 ** 2 - 2 * math.log(x2) - 1


def f2(x1, x2):
    return x1 ** 2 - x1 * x2 + 1


def phi1(x1, x2):
    return math.sqrt(2 * math.log(x2) + 1)


def phi2(x1, x2):
    return x1 + 1 / x1


def simple_iteration(x1, x2, eps):
    q = 1 - 1 / 1.75 ** 2
    count = 0
    errors = []

    while True:
        new_x1 = phi1(x1, x2)
        new_x2 = phi2(x1, x2)
        count += 1

        diff = max(abs(new_x1 - x1), abs(new_x2 - x2))
        error = q / (1 - q) * diff
        errors.append(error)

        if error < eps:
            return new_x1, new_x2, count, errors

        x1 = new_x1
        x2 = new_x2


def newton(x1, x2, eps):
    count = 0
    errors = []

    while True:
        a = 2 * x1
        b = -2 / x2
        c = 2 * x1 - x2
        d = -x1

        det = a * d - b * c

        dx1 = (-f1(x1, x2) * d + b * f2(x1, x2)) / det
        dx2 = (-a * f2(x1, x2) + c * f1(x1, x2)) / det

        new_x1 = x1 + dx1
        new_x2 = x2 + dx2
        count += 1

        error = max(abs(dx1), abs(dx2))
        errors.append(error)

        if error < eps:
            return new_x1, new_x2, count, errors

        x1 = new_x1
        x2 = new_x2


eps = float(input("Epsilon: "))

x1 = 1.6
x2 = 2.2

a1, a2, count1, errors1 = simple_iteration(x1, x2, eps)
b1, b2, count2, errors2 = newton(x1, x2, eps)

print("\nInitial approximation:")
print(f"x1 = {x1}, x2 = {x2}")

print("\nSimple iteration:")
print(f"x1 = {a1:.6f}")
print(f"x2 = {a2:.6f}")
print(f"Iterations: {count1}")

print("\nError by iteration:")
for i in range(len(errors1)):
    print(f"{i + 1}: {errors1[i]:.10f}")

print("\nNewton method:")
print(f"x1 = {b1:.6f}")
print(f"x2 = {b2:.6f}")
print(f"Iterations: {count2}")

print("\nError by iteration:")
for i in range(len(errors2)):
    print(f"{i + 1}: {errors2[i]:.10f}")