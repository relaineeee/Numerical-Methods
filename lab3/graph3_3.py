import numpy as np
import matplotlib.pyplot as plt
from lab3_3 import least_squares, polynomial
from data.data3_3 import X, Y


x = X
y = Y

a1 = least_squares(x, y, 1)
a2 = least_squares(x, y, 2)
a3 = least_squares(x, y, 3)

xx = np.linspace(min(x), max(x), 500)

plt.scatter(x, y, label="Data points")
plt.plot(xx, [polynomial(a1, xi) for xi in xx], label="Degree 1")
plt.plot(xx, [polynomial(a2, xi) for xi in xx], label="Degree 2")
plt.plot(xx, [polynomial(a3, xi) for xi in xx], label="Degree 3")

plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.savefig("graph3_3.png", dpi=300)
plt.show()