import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

def k_imbalance(x):
    x = np.ravel(x)[0] if np.ndim(x) else x
    return (2*x)**2 / ((a - x)*(b - x)) - K

x_newton = newton(k_imbalance, 0.5)
res = minimize(lambda x: k_imbalance(x)**2, x0=[0.5],
               method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]

print(f"Newton: x = {x_newton:.5f}")
print(f"SLSQP : x = {x_slsqp:.5f}")
print("Agree:", np.isclose(x_newton, x_slsqp, atol=1e-3))

x = x_newton
print(f"Equilibrium: H2 = {a-x:.3f} mol, I2 = {b-x:.3f} mol, HI = {2*x:.3f} mol")

xs = np.linspace(0, 0.999, 400)
plt.plot(xs, a - xs, label="H2")
plt.plot(xs, b - xs, "--", label="I2")
plt.plot(xs, 2*xs, label="HI")
plt.axvline(x, color="k", ls=":", label=f"equilibrium x = {x:.3f}")
plt.xlabel("extent x (mol)")
plt.ylabel("amount (mol)")
plt.title("H2 + I2 <=> 2 HI")
plt.legend()
plt.savefig("equilibrium.png", dpi=150, bbox_inches="tight")