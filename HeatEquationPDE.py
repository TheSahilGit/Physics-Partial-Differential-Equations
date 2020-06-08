"""Problem: To solve 1D heat equation by explicit scheme.
    Initial conditions are:
    i. u(x,0)=100*Sin(pi*x)
    ii. u(0,t)=u(1,t)=0
    """
### Sahil Islam ###
### 08/06/2020 ###


import matplotlib.pyplot as plt
import numpy as np

nx = 10
nt = 15000

k = 4.
dx = float(1/nx)
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

for k in range(0, int(nx / 2) + 1):
    plt.plot(ts, u[k, :], label='Position=' + str(k))

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.grid()
plt.legend()
plt.show()

mint = 0
maxt = int(nt)
plots = 10
interval = int((maxt - mint) / plots)

for k in range(mint, maxt, interval):
    plt.plot(xs, u[:, k], label='Time=' + str(k))

plt.xlabel("Position")
plt.ylabel("Temperature")
plt.grid()
plt.legend()
plt.show()

