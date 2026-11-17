import math

X_NODES_A = [-0.4, -0.1, 0.2, 0.5]
X_NODES_B = [-0.4, 0.0, 0.2, 0.5]
X_STAR = 0.1


def f(x):
    return math.asin(x) + x
