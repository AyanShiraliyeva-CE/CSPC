## PW2 --- Lab B

### Part 2: three routes to a minimum
- **2A, f(x) = (x-3)^2 + 1:** gradient descent, Newton and SLSQP all reach x = 3. On an easy convex function the methods agree.
- **2B, g(x) = x^4 - 3x^2 + x + 5** (several stationary points):

| start | gradient descent | Newton (g'(x)=0) | SLSQP |
|-------|------------------|------------------|-------|
| x0 = 0 | x = -1.301 (min) | x = 0.170, g'' = -5.65 -> **maximum** | x = -1.301 (min) |
| x0 = 2 | x = 1.131 (local min) | x = 1.131, g'' = 9.35 -> minimum | x = -1.301 (global min) |

  - The methods do **not** always agree on g.
  - From x0 = 0, Newton landed on a maximum: it only finds a stationary point, so the sign of g'' must be checked.
  - The starting point and the algorithm change the result. The global minimum is x = -1.301 (g = 1.486), the local minimum is x = 1.131 (g = 3.930).

### Part 3: reaction rate
Fitted first-order rate constant: **k = 0.262** (SLSQP, bounds (0, 5), x0 = 0.5). Close to the expected 0.25; the difference comes from measurement noise. Plot: `PW2/Lab B/kinetics.png`.

### Part 4: equilibrium (H2 + I2 <=> 2 HI, K = 15.6)
Newton and SLSQP agree: extent **x = 0.664**. Composition: H2 = 0.336 mol, I2 = 0.336 mol, **HI = 1.328 mol**. Plot: `PW2/Lab B/equilibrium.png`.

### Part 5 (bonus): titration
Equivalence point (maximum of dpH/dV): **50.0 mL**. Plot: `PW2/Lab B/titration.png`.
