import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
x = np.linspace(0, 10, 10)
y1 = np.sin(x)
y2 = np.sin(x ** 2)
y3 = 0.1*x
plt.figure(figsize=(8, 4))

plt.title("sin(x) and sin(x**2)")
plt.plot(x, y1, label="sin(x)", color="r", linewidth=2)
plt.plot(x, y2, label="sin(x**2)", color="b", linewidth=2)
plt.scatter(x, y2, label="sin(x**2)")
plt.bar(x, y2, label="sin(x**2)")
plt.ylim(-1.5, 1.5)
plt.xlim(0, 10)
plt.legend()

plt.show()
