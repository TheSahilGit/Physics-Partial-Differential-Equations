import matplotlib.pyplot as plt
import numpy as np

nx = 10
nt = 10000

k = 4.
dx = 0.1
dt = 0.000001
a = float(k * dt / (dx * dx))

u = np.zeros((nx + 1, nt + 1))
xs = []
ts = []

for i in range(nx + 1):
    x = i * dx
    u[i, 0] = 100.0 * np.sin(np.pi * x)
    xs.append(x)

for j in range(nt + 1):
    t = j * dt
    u[0, j] = 0
    u[10, j] = 0
    ts.append(t)

for i in range(1, nx):
    for j in range(nt):
        u[i, j + 1] = a * u[i - 1, j] + (1 - 2 * a) * u[i, j] + a * u[i + 1, j]

for k in range(0, int(nx/2)+1):
    plt.plot(ts, u[k, :], label='x=' + str(k))

plt.grid()
plt.legend()
plt.show()

for k in range(000, int(nt/10), 100):
    plt.plot(xs, u[:, k], label='t=' + str(k))

plt.grid()
plt.legend()
plt.show()
