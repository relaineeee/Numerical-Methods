
import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return x ** 4


def f2(x):
    return 2 * x + 1


x = np.linspace(1.0, 1.6, 500)

plt.plot(x, f1(x), label=r'$y_1 = x^4$')
plt.plot(x, f2(x), label=r'$y_2 = 2x + 1$')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.savefig('graph_2_1.png', dpi=300)
plt.show()
