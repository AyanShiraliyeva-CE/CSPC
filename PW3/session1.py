import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("Heart_disease_cleveland_new.csv")
print(df.shape)
print(df.head())

cols = ["age", "chol", "trestbps", "thalach"]
data = df[cols]
print(data.describe())

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, c in zip(axes.flat, cols):
    ax.hist(data[c], bins=20, edgecolor="black")
    ax.set_title(c)
plt.tight_layout()
plt.savefig("distributions.png", dpi=150)
plt.close()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, c in zip(axes.flat, cols):
    stats.probplot(data[c], dist="norm", plot=ax)
    ax.set_title(c)
plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)
plt.close()

for c in cols:
    w, p = stats.shapiro(data[c])
    print(c, "W =", round(w, 3), "p =", round(p, 4), "skew =", round(stats.skew(data[c]), 2))