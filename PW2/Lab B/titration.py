import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V, pH = data[:, 0], data[:, 1]

slope = np.gradient(pH, V)
i = np.argmax(slope)
V_eq = V[i]
print(f"Equivalence point: {V_eq:.1f} mL (max slope = {slope[i]:.2f} pH/mL)")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.plot(V, pH)
ax1.axvline(V_eq, color="r", ls="--", label=f"{V_eq:.0f} mL")
ax1.set_xlabel("volume of base (mL)")
ax1.set_ylabel("pH")
ax1.legend()
ax1.set_title("Titration curve")
ax2.plot(V, slope)
ax2.axvline(V_eq, color="r", ls="--")
ax2.set_xlabel("volume of base (mL)")
ax2.set_ylabel("dpH/dV")
ax2.set_title("Slope (peaks at equivalence)")
fig.savefig("titration.png", dpi=150, bbox_inches="tight")