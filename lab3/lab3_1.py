from data.data3_1 import X_NODES_A, X_NODES_B, X_STAR, f


def lagrange(x, y, val):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (val - x[j]) / (x[i] - x[j])
        result += term
    return result


def differences(x, y):
    n = len(x)
    table = [[0.0] * n for i in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i][j - 1] - table[i + 1][j - 1]) / (x[i] - x[i + j])
    return table


def newton(x, table, val):
    n = len(x)
    result = table[0][0]
    term = 1
    for i in range(1, n):
        term *= val - x[i - 1]
        result += table[0][i] * term
    return result


def lagrange_text(x, y):
    parts = []
    for i in range(len(x)):
        den = 1
        factors = []
        for j in range(len(x)):
            if i != j:
                den *= x[i] - x[j]
                factors.append(f"(x - ({x[j]:g}))")
        coef = y[i] / den
        parts.append(f"({coef:.10f}) * " + " * ".join(factors))
    return " +\n".join(parts)


def newton_text(x, table):
    parts = [f"{table[0][0]:.10f}"]
    for i in range(1, len(x)):
        factors = []
        for j in range(i):
            factors.append(f"(x - ({x[j]:g}))")
        parts.append(f"({table[0][i]:.10f}) * " + " * ".join(factors))
    return " +\n".join(parts)


def solve(x, val):
    y = [f(xi) for xi in x]
    table = differences(x, y)
    l = lagrange(x, y, val)
    n = newton(x, table, val)
    exact = f(val)

    print("\nInterpolation nodes:")
    print("i          x              y")
    for i in range(len(x)):
        print(f"{i:<5} {x[i]:10.4f} {y[i]:14.10f}")

    print("\nLagrange polynomial:")
    print("L(x) = " + lagrange_text(x, y))

    print("\nDivided differences:")
    for i in range(len(x)):
        print("  ".join(
            f"{table[i][j]:14.10f}"
            for j in range(len(x) - i)
        ))

    print("\nNewton polynomial:")
    print("N(x) = " + newton_text(x, table))

    print(f"\nx* = {val}")
    print(f"L(x*) = {l:.10f}")
    print(f"N(x*) = {n:.10f}")
    print(f"f(x*) = {exact:.10f}")
    print(f"Lagrange error = {abs(exact - l):.10f}")
    print(f"Newton error = {abs(exact - n):.10f}")
    print(f"Methods difference = {abs(l - n):.12f}")


def main():
    x1 = X_NODES_A
    x2 = X_NODES_B
    val = X_STAR

    print("Case A")
    solve(x1, val)
    print("\n" + "=" * 50)
    print("Case B")
    solve(x2, val)


if __name__ == "__main__":
    main()