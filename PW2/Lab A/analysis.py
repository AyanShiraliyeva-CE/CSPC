import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1:
t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)

# TODO 2: 
v = np.gradient(y, t)
a = np.gradient(v, t)

print("Mean acceleration:", np.mean(a))
print("Acceleration standard deviation:", np.std(a))

# TODO 3:
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

print("Largest difference in position:",
      np.max(np.abs(y_recovered - y)))

# TODO 4: 
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")
axes[0].set_title("Position vs Time")
axes[0].grid()

axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")
axes[1].set_title("Velocity vs Time")
axes[1].grid()

axes[2].plot(t, a)
axes[2].axhline(-9.81, linestyle="--", label="True -9.81 m/s²")
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].set_title("Acceleration vs Time")
axes[2].legend()
axes[2].grid()

plt.tight_layout()
plt.savefig("motion.png")
plt.show()