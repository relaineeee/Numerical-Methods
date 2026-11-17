import numpy as np
import matplotlib.pyplot as plt
from lab3_2 import spline, calc
from data.data3_2 import X, Y, X_STAR

x = X
y = Y
t = X_STAR

a, b, c, d = spline(x, y)
for i in range(len(a)):
    xx = np.linspace(x[i], x[i + 1], 100)
    yy = [calc(x, a, b, c, d, z) for z in xx]
    plt.plot(xx, yy, color='C0', label='Cubic spline' if i == 0 else None)

plt.scatter(x, y, color='C1', label='Nodes', zorder=3)
plt.scatter([t], [calc(x, a, b, c, d, t)], color='C2', label='x*', zorder=4)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.savefig('graph3_2.png', dpi=300)
plt.show()
