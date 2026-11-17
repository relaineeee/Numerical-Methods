def f(x):
    return x ** 4 - 2 * x - 1


def df(x):
    return 4 * x ** 3 - 2


def phi(x):
    return (2 * x + 1) ** 0.25


def dphi(x):
    return 1 / (2 * (2 * x + 1) ** 0.75)


def simple_iteration(x, a, eps):
    q = abs(dphi(a))
    count = 0
    errors = []

    while True:
        new_x = phi(x)
        count += 1

        error = q / (1 - q) * abs(new_x - x)
        errors.append(error)

        if error < eps:
            return new_x, count, errors

        x = new_x


def newton(x, eps):
    count = 0
    errors = []

    while True:
        new_x = x - f(x) / df(x)
        count += 1

        error = abs(new_x - x)
        errors.append(error)

        if error < eps:
            return new_x, count, errors

        x = new_x


eps = float(input("Epsilon: "))

a = 1.3
b = 1.4
x0 = b

x1, count1, errors1 = simple_iteration(x0, a, eps)
x2, count2, errors2 = newton(x0, eps)

print("\nInterval:")
print(f"[{a}, {b}]")
print(f"Initial approximation: {x0}")

print("\nSimple iteration:")
print(f"x = {x1:.10f}")
print(f"Iterations: {count1}")

print("\nError by iteration:")
for i in range(len(errors1)):
    print(f"{i + 1}: {errors1[i]:.10f}")

print("\nNewton method:")
print(f"x = {x2:.10f}")
print(f"Iterations: {count2}")

print("\nError by iteration:")
for i in range(len(errors2)):
    print(f"{i + 1}: {errors2[i]:.10f}")