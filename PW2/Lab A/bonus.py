import numpy as np
import matplotlib.pyplot as plt

# Read trajectory data
t, x, y = np.loadtxt(
    "trajectory.csv",
    delimiter=",",
    skiprows=1,
    unpack=True
)

# Calculate velocity components
vx = np.gradient(x, t)
vy = np.gradient(y, t)

# Calculate speed
speed = np.sqrt(vx**2 + vy**2)

# Print average speed
print("Mean speed:", np.mean(speed))

# Plot 2D trajectory
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("2D Trajectory")
plt.grid()
plt.axis("equal")
plt.tight_layout()
plt.savefig("trajectory.png")

# Plot speed vs time
plt.figure(figsize=(8, 6))
plt.plot(t, speed)
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Speed vs Time")
plt.grid()
plt.tight_layout()
plt.savefig("speed.png")

plt.show()
