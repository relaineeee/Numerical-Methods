from math import sqrt, log, atan
from data.data3_5 import A, B, H1, H2, f


def left_rectangles(a, b, h):
    n = round((b - a) / h)
    result = 0
    for i in range(n):
        result += f(a + i * h)
    return result * h


def right_rectangles(a, b, h):
    n = round((b - a) / h)
    result = 0
    for i in range(1, n + 1):
        result += f(a + i * h)
    return result * h


def rectangles(a, b, h):
    n = round((b - a) / h)
    result = 0
    for i in range(n):
        x = a + (i + 0.5) * h
        result += f(x)
    return result * h


def trapezoids(a, b, h):
    n = round((b - a) / h)
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return result * h


def simpson(a, b, h):
    n = round((b - a) / h)
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)
    return result * h / 3


def runge_romberg(i1, i2, h1, h2, p):
    correction = (i2 - i1) / ((h1 / h2) ** p - 1)
    return abs(correction), i2 + correction


def antiderivative(x):
    s = sqrt(2)
    t1 = s / 40 * log((x * x - 5 * s * x + 25) / (x * x + 5 * s * x + 25))
    t2 = s / 20 * (atan(s * x / 5 - 1) + atan(s * x / 5 + 1))
    return t1 + t2


def main():
    a = A
    b = B
    h1 = H1
    h2 = H2
    exact = antiderivative(b) - antiderivative(a)
    print(f'Integration interval: [{a}, {b}]')
    print(f'h1 = {h1}, h2 = {h2}')
    print('f(x) = x^2 / (625 + x^4)')
    print(f'Exact integral = {exact:.12f}')
    print('\n' + f"{'Method':<21} {'I(h1)':>14} {'I(h2)':>14} {'p':>3} {'Refined':>14} {'RR error':>14} {'Abs err h2':>14} {'Abs err ref':>14}")
    print('-' * 118)

    best_name = ''
    best_error = float('inf')
    for name, method, p in [
        ('Left rectangles', left_rectangles, 1),
        ('Right rectangles', right_rectangles, 1),
        ('Midpoint rectangles', rectangles, 2),
        ('Trapezoids', trapezoids, 2),
        ('Simpson', simpson, 4)
    ]:
        i1 = method(a, b, h1)
        i2 = method(a, b, h2)
        error, refined = runge_romberg(i1, i2, h1, h2, p)
        abs_error_h2 = abs(exact - i2)
        abs_error_ref = abs(exact - refined)
        print(f'{name:<21} {i1:14.10f} {i2:14.10f} {p:3d} {refined:14.10f} {error:14.10f} {abs_error_h2:14.10f} {abs_error_ref:14.10f}')
        if abs_error_h2 < best_error:
            best_error = abs_error_h2
            best_name = name
    print(f'\nMost accurate method for h2: {best_name}')
    print(f'Absolute error: {best_error:.12f}')


if __name__ == '__main__':
    main()
