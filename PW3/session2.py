import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("Heart_disease_cleveland_new.csv")

disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]
print(len(disease), len(healthy))

t, p_t = stats.ttest_ind(disease, healthy, equal_var=False)
print("Welch t-test:", t, p_t)

u, p_u = stats.mannwhitneyu(disease, healthy)
print("Mann-Whitney:", u, p_u)

means = [disease.mean(), healthy.mean()]
sems = [stats.sem(disease), stats.sem(healthy)]
print(means, sems)

plt.errorbar([0, 1], means, yerr=[1.96 * s for s in sems], fmt="o", capsize=6)
plt.xticks([0, 1], ["disease", "healthy"])
plt.ylabel("thalach (mean ± 95% CI)")
plt.savefig("thalach_means.png", dpi=150)
plt.close()

r, p_r = stats.pearsonr(df["age"], df["thalach"])
rho, p_rho = stats.spearmanr(df["age"], df["thalach"])
print("Pearson:", r, p_r)
print("Spearman:", rho, p_rho)

plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.xlabel("age")
plt.ylabel("thalach")
plt.savefig("age_thalach.png", dpi=150)
plt.close()

props = df["target"].value_counts(normalize=True)
print(props)
entropy = -(props * np.log2(props)).sum()
print("Entropy:", entropy)