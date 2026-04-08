import numpy as np
try:
    data = np.loadtxt('sample.csv', delimiter=',')
except OSError:
    data = np.random.uniform(50, 100, size=75)
B = 500
bootstrap_means = []
rng = np.random.default_rng(seed=42)
for _ in range(B):
    sample = rng.choice(data, size=len(data), replace=True)
    bootstrap_means.append(sample.mean())
bootstrap_means = np.array(bootstrap_means)
lower = np.percentile(bootstrap_means, 2.5)
upper = np.percentile(bootstrap_means, 97.5)
print(f"Бутстреп-орта мәндерінің саны: {len(bootstrap_means)}")
print(f"95% сенімділік аралығы: [{lower:.4f}, {upper:.4f}]")
