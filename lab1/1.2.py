def read_data(fname):
    with open(fname, "r") as f:
        data = [[float(x) for x in line.split()] for line in f]

    a = [row[0] for row in data]
    b = [row[1] for row in data]
    c = [row[2] for row in data]
    d = [row[3] for row in data]

    return a, b, c, d


def sweep(a, b, c, d):
    n = len(b)
    p = [0.0 for i in range(n)]
    q = [0.0 for i in range(n)]

    p[0] = -c[0] / b[0]
    q[0] = d[0] / b[0]

    for i in range(1, n):
        den = b[i] + a[i] * p[i - 1]
        p[i] = -c[i] / den
        q[i] = (d[i] - a[i] * q[i - 1]) / den

    x = [0.0 for i in range(n)]
    x[n - 1] = q[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = p[i] * x[i + 1] + q[i]

    return p, q, x


a, b, c, d = read_data("sweep.txt")
p, q, x = sweep(a, b, c, d)

print("Sweep coefficients:")
for i in range(len(p)):
    print(f"p{i + 1} = {p[i]:.6f}, q{i + 1} = {q[i]:.6f}")

print("\nSolution:")
for i in range(len(x)):
    print(f"x{i + 1} = {x[i]:.6f}")