import numpy as np
import matplotlib.pyplot as plt

a = 0.9
b = 0.5
epsilon = 0.08
Ip = 1

T = 200
dt = 0.01
t = np.arange(0, T, dt)

v = np.zeros(len(t))
w = np.zeros(len(t))

v[0] = 0
w[0] = 0

for i in range(len(t) - 1):
    dv = v[i] - v[i]**3 / 3 - w[i] + Ip
    dw = epsilon * (v[i] + a - b * w[i])
    v[i + 1] = v[i] + dt * dv
    w[i + 1] = w[i] + dt * dw

v_plot = np.linspace(-2.5, 2.5, 500)
w_null2 = (v_plot + a) / b
w_null_v = v_plot - v_plot**3 / 3 + Ip

plt.figure(figsize=(5, 5))
plt.plot(v_plot, w_null_v, label="dv/dt = 0")
plt.plot(v_plot, w_null2, label="dw/dt = 0")
plt.plot(v, w, alpha=0.6, label="Trajectoire")
plt.xlabel("Potentiel membranaire v")
plt.ylabel("Variable de récupération w")
plt.ylim(-1,3)
plt.legend()
plt.grid()
plt.show()