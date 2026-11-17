from data.data3_4 import X, Y, X_STAR


def derivative(x, y, val):
    i = x.index(val)
    left = (y[i] - y[i - 1]) / (x[i] - x[i - 1])
    right = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    d1 = left + (right - left) * (2 * val - x[i - 1] - x[i]) / (x[i + 1] - x[i - 1])
    d2 = 2 * (right - left) / (x[i + 1] - x[i - 1])
    return d1, d2


def main():
    x = X
    y = Y
    val = X_STAR
    print('Original table:')
    print('i          x              y')
    for i in range(len(x)):
        print(f'{i:<5} {x[i]:10.4f} {y[i]:14.10f}')
    print(f'\nx* = {val}')
    print('\nNodes used for differentiation:')
    print('i          x              y')
    i = x.index(val)
    for j in range(i - 1, i + 2):
        print(f'{j:<5} {x[j]:10.4f} {y[j]:14.10f}')
    d1, d2 = derivative(x, y, val)
    print(f"\nf'(x*) = {d1:.10f}")
    print(f"f''(x*) = {d2:.10f}")


if __name__ == '__main__':
    main()
