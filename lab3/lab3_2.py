from data.data3_2 import X, Y, X_STAR


def spline(x, y):
    n = len(x) - 1
    h = [x[i] - x[i - 1] for i in range(1, n + 1)]

    m = n - 1
    lower = [0.0] * m
    diag = [0.0] * m
    upper = [0.0] * m
    rhs = [0.0] * m

    for j in range(m):
        i = j + 1
        lower[j] = h[i - 1] if j > 0 else 0.0
        diag[j] = 2 * (h[i - 1] + h[i])
        upper[j] = h[i] if j < m - 1 else 0.0
        rhs[j] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    p = [0.0] * m
    q = [0.0] * m
    for j in range(m):
        den = diag[j] + lower[j] * p[j - 1] if j else diag[j]
        p[j] = -upper[j] / den
        q[j] = (rhs[j] - lower[j] * q[j - 1]) / den if j else rhs[j] / den

    c = [0.0] * (n + 1)
    for j in range(m - 1, -1, -1):
        c[j + 2] = p[j] * c[j + 3] + q[j] if j < m - 1 else q[j]

    a = [y[i - 1] for i in range(1, n + 1)]
    b = [0.0] * n
    d = [0.0] * n
    for i in range(1, n):
        b[i - 1] = (y[i] - y[i - 1]) / h[i - 1] - h[i - 1] * (c[i + 1] + 2 * c[i]) / 3
        d[i - 1] = (c[i + 1] - c[i]) / (3 * h[i - 1])
    b[n - 1] = (y[n] - y[n - 1]) / h[n - 1] - 2 * h[n - 1] * c[n] / 3
    d[n - 1] = -c[n] / (3 * h[n - 1])

    return a, b, c[1:], d


def calc(x, a, b, c, d, t):
    i = len(a) - 1
    for j in range(len(a)):
        if t <= x[j + 1]:
            i = j
            break
    dx = t - x[i]
    return a[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3


def main():
    x = X
    y = Y
    t = X_STAR

    print('Interpolation nodes:')
    print(f"{'i':<5} {'x':>10} {'y':>14}")
    for i in range(len(x)):
        print(f'{i:<5} {x[i]:10.4f} {y[i]:14.5f}')

    a, b, c, d = spline(x, y)
    print('\nSpline coefficients (formula 3.14):')
    print(f"{'i':<5} {'Interval':<15} {'a':>12} {'b':>12} {'c':>12} {'d':>12}")
    for i in range(len(a)):
        interval = f'[{x[i]:.2f}, {x[i + 1]:.2f}]'
        print(f'{i + 1:<5} {interval:<15} {a[i]:12.8f} {b[i]:12.8f} {c[i]:12.8f} {d[i]:12.8f}')

    k = next(i for i in range(len(a)) if t <= x[i + 1])
    print(f'\nx* = {t}')
    print(f'Interval: {k + 1} [{x[k]}, {x[k + 1]}]')
    print(f'S(x*) = {calc(x, a, b, c, d, t):.10f}')

    print('\nNode verification:')
    for i in range(len(x)):
        print(f'x = {x[i]:.2f}, S(x) = {calc(x, a, b, c, d, x[i]):.8f}, y = {y[i]:.8f}')

    print('\nBoundary conditions:')
    print(f"S''({x[0]}) = {2 * c[0]:.10f}")
    hn = x[-1] - x[-2]
    print(f"S''({x[-1]}) = {2 * c[-1] + 6 * d[-1] * hn:.10f}")


if __name__ == '__main__':
    main()
