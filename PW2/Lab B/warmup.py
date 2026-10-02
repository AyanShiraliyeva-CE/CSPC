import numpy as np
from scipy.optimize import newton, minimize

def gradient_descent(df, x0, lr, tol=1e-10, max_iter=100000):
    x = x0
    for _ in range(max_iter):
        step = lr * df(x)
        x = x - step
        if abs(step) < tol:
            break
    return x

def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

print("=== 2A: f(x) = (x-3)^2 + 1, x0 = 0 ===")
print("gradient descent:", gradient_descent(df, 0.0, lr=0.1))
print("Newton          :", newton(df, 0.0, fprime=d2f))
print("SLSQP           :", minimize(f, x0=[0.0], method="SLSQP").x[0])

def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

print("\n=== 2B: g(x) = x^4 - 3x^2 + x + 5 ===")
for x0 in (0.0, 2.0):
    print(f"\n--- start x0 = {x0} ---")
    x_gd = gradient_descent(dg, x0, lr=0.01)
    x_nt = newton(dg, x0, fprime=d2g)
    x_sl = minimize(g, x0=[x0], method="SLSQP").x[0]
    print(f"gradient descent: x = {x_gd:.6f}, g = {g(x_gd):.6f}")
    kind = "minimum" if d2g(x_nt) > 0 else "maximum"
    print(f"Newton          : x = {x_nt:.6f}, g = {g(x_nt):.6f}, g'' = {d2g(x_nt):.3f} -> {kind}")
    print(f"SLSQP           : x = {x_sl:.6f}, g = {g(x_sl):.6f}")