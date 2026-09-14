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
