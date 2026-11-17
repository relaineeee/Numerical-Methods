import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return np.exp((x ** 2 - 1) / 2)


def f2(x):
    return x + 1 / x


x = np.linspace(1.3, 1.9, 500)

plt.plot(x, f1(x), label=r'$x_2 = e^{(x_1^2 - 1)/2}$')
plt.plot(x, f2(x), label=r'$x_2 = x_1 + 1/x_1$')

plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(True)
plt.legend()

plt.savefig('graph_2_2.png', dpi=300)
plt.show()