from data.data3_3 import X, Y


def solve_system(a, b):
    n = len(b)
    for i in range(n):
        k = max(range(i, n), key=lambda j: abs(a[j][i]))
        a[i], a[k] = a[k], a[i]
        b[i], b[k] = b[k], b[i]
        for j in range(i + 1, n):
            t = a[j][i] / a[i][i]
            for m in range(i, n):
                a[j][m] -= t * a[i][m]
            b[j] -= t * b[i]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]
    return x


def least_squares(x, y, degree):
    n = degree + 1
    a = [[sum(xi ** (i + j) for xi in x) for j in range(n)] for i in range(n)]
    b = [sum(yi * xi ** i for xi, yi in zip(x, y)) for i in range(n)]
    return solve_system(a, b)


def polynomial(a, x):
    return sum(coef * x ** i for i, coef in enumerate(a))


def polynomial_text(a):
    return ' + '.join(f'({coef:.8f})' + (f' * x^{i}' if i > 1 else ' * x' if i == 1 else '') for i, coef in enumerate(a))


def main():
    x = X
    y = Y
    errors = []

    for degree in (1, 2, 3):
        a = least_squares(x, y, degree)
        mse = sum((polynomial(a, xi) - yi) ** 2 for xi, yi in zip(x, y)) / len(x)
        errors.append(mse)
        print(f'Polynomial degree {degree}:')
        for i, coef in enumerate(a):
            print(f'a{i} = {coef:.10f}')
        print(f'P{degree}(x) = {polynomial_text(a)}')
        print(f'MSE{degree} = {mse:.10f}')
        print('i          x              y           P(x)')
        for i, (xi, yi) in enumerate(zip(x, y)):
            print(f'{i:<5} {xi:10.4f} {yi:14.5f} {polynomial(a, xi):14.5f}')
        print()

    print('MSE comparison:')
    for i, mse in enumerate(errors, 1):
        print(f'MSE{i} = {mse:.10f}')
    print(f'Best approximation: P{errors.index(min(errors)) + 1}(x)')


if __name__ == '__main__':
    main()
