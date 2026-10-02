<<<<<<< HEAD
# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation (pure-Python loop and NumPy vectorised versions), a pytest test suite, and a speed comparison script.

**Speed comparison (loop vs NumPy):**
- loop  : 2.5065 s
- numpy : 0.0002 s
- speed-up: 11542.4x faster

**Tests:** all passing? yes

**Conclusion:**
- The NumPy vectorised version is dramatically faster than the pure-Python loop because it replaces per-atom Python-level iteration with a single vectorised binomial draw across all surviving atoms at once. This showed me how much overhead plain Python loops carry compared to array operations. Setting up conda, git branching, and pushing to GitHub also helped me understand the full reproducible workflow.


## PW1 --- Lab B

The observed data shows an exponential decay from about 5000 counts at t=0 
down to roughly 330 counts by t=9. Comparing the observed data (scatter) 
to the analytical curve N0*exp(-λt) with λ=0.3, the two shapes match closely, 
confirming the data follows the expected exponential decay law.

The Snakemake pipeline (Snakefile) has one rule that regenerates figure.png 
from decay_observed.csv by running plot.py, and only reruns it when the 
input data or script changes.
=======
## PW2 --- Lab A

### Results

- Mean acceleration: -8.58 m/s²
- Acceleration standard deviation: 28.72 m/s²
- Largest difference in recovered position: 0.785 m

### Noise observation

The acceleration is much noisier than the position because differentiation amplifies measurement noise. Since acceleration is obtained by differentiating the position data twice, the noise becomes much larger.

### Integration back

I integrated the noisy acceleration back to velocity and then to position. The recovered position was close to the original position, with a largest difference of 0.785 m. This shows that integration suppresses some of the noise.

## Bonus --- 2D Trajectory

### Results

- Mean speed: 23.65 m/s

### Analysis

The trajectory data contains the x and y positions of the object over time. I calculated the velocity components using numerical differentiation and then calculated the total speed from the x and y components.

The mean speed was 23.65 m/s. I also generated a 2D trajectory plot and a speed-versus-time plot.
>>>>>>> 43861ef (PW2 Lab A: motion analysis and bonus)
