import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("chemicals_cancer.csv")
print(df.columns)
print(df.shape)

col_b = "benzene"
col_c = "cadmium"
col_m = "malignancy"
col_p = "pollution_index"

print("naive")
print(df[col_b].corr(df[col_m]))
print(df[col_c].corr(df[col_m]))

lo, hi = 40, 60
sub = df[(df[col_p] > lo) & (df[col_p] < hi)]
print(len(sub))

print("controlled")
print(sub[col_b].corr(sub[col_m]))
print(sub[col_c].corr(sub[col_m]))

print("all correlations")
print(df.corr())

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].scatter(df[col_b], df[col_m], alpha=0.4)
axes[0, 0].set_title("benzene, all patients")
axes[0, 1].scatter(df[col_c], df[col_m], alpha=0.4)
axes[0, 1].set_title("cadmium, all patients")
axes[1, 0].scatter(sub[col_b], sub[col_m], alpha=0.4)
axes[1, 0].set_title("benzene, pollution 40-60")
axes[1, 1].scatter(sub[col_c], sub[col_m], alpha=0.4)
axes[1, 1].set_title("cadmium, pollution 40-60")

for ax in axes.flat:
    ax.set_ylabel("malignancy")

plt.tight_layout()
plt.savefig("chem_scatter.png", dpi=150)
plt.close()