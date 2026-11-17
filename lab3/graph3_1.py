import numpy as np
import matplotlib.pyplot as plt

from lab3_1 import lagrange, newton, differences
from data.data3_1 import X_NODES_A, X_NODES_B, X_STAR, f


x1 = X_NODES_A
x2 = X_NODES_B
val = X_STAR

for name, x in [("A", x1), ("B", x2)]:
    y = [f(xi) for xi in x]
    table = differences(x, y)

    xx = np.linspace(-0.5, 0.6, 500)

    yy = [f(t) for t in xx]
    ll = [lagrange(x, y, t) for t in xx]
    nn = [newton(x, table, t) for t in xx]

    plt.figure()

    plt.plot(xx, yy, label="f(x) = arcsin(x) + x")
    plt.plot(xx, ll, "--", label="Lagrange")
    plt.plot(xx, nn, ":", label="Newton")
    plt.scatter(x, y, label="Nodes", zorder=5)
    plt.scatter(val, f(val), label="x*", zorder=6)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Case {name}")
    plt.grid(True)
    plt.legend()

    plt.savefig(f"graph_3_1_{name}.png", dpi=300)
    plt.show()