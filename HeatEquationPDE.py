"""Problem: To solve 1D heat equation by explicit scheme.
    Initial conditions are:
    i. u(x,0)=100*Sin(pi*x)
    ii. u(0,t)=u(1,t)=0
    """
### Sahil Islam ###
### 08/06/2020 ###

import matplotlib.pyplot as plt
import numpy as np

kx = 11
kt = 10 ** 5
temp = np.zeros((kx, kt))
time = np.zeros(kt)
position = np.linspace(0, 1, kx)

k = 4.0
dx = 0.1
dt = 1. / (10 ** 5)
c = k * dt / dx ** 2

ti = np.linspace(0, 50000, kt)

for t in range(kt - 1):
    time[t + 1] = time[t] + t * dt

for t in range(kt - 1):
    for x in range(1, kx - 1):
        temp[x, t] = 100. * np.sin(np.pi * position[x])

for t in range(kt - 1):
    for x in range(1, kx - 1):
        temp[x, t + 1] = temp[x, t] + c * (temp[x + 1, t] - 2 * temp[x, t] + temp[x - 1, t])

for k in range(0, kx - 1):
    plt.plot(time, temp[k, :], label='Position=' + str(k))

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.grid()
plt.legend()
plt.show()

mint = 0
maxt = 10000
plots = 10
interval = int((maxt - mint) / plots)

for k in range(mint, maxt, interval):
    plt.plot(position, temp[:, k], label='Time=' + str(k))

plt.xlabel("Position")
plt.ylabel("Temperature")
plt.grid()
plt.legend()
plt.show()
