"""
Compare the speed of the pure-Python loop version vs the NumPy vectorised
version of the decay simulation.
"""

import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

# --- Pure-Python loop version ---
start = time.perf_counter()
simulate_loop(N0, lam)
loop_time = time.perf_counter() - start

# --- NumPy vectorised version ---
start = time.perf_counter()
simulate(N0, lam)
numpy_time = time.perf_counter() - start

print(f"Loop  (pure Python): {loop_time:.4f} s")
print(f"NumPy (vectorised):  {numpy_time:.4f} s")
print(f"NumPy is {loop_time / numpy_time:.1f}x faster")
