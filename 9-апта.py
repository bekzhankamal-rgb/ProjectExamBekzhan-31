import numpy as np
try:
    data = np.loadtxt('sample.csv', delimiter=',')
except:
    rng = np.random.default_rng(seed=42)
    data = rng.uniform(10, 100, size=75)
    print("Ескерту: 'sample.csv' табылмады, тесттік деректер қолданылды.\n")
B = 500  # Репликация саны
rng = np.random.default_rng()
bootstrap_means = np.array([
    np.mean(rng.choice(data, size=len(data), replace=True))
    for _ in range(B)
])
lower_bound = np.percentile(bootstrap_means, 2.5)
upper_bound = np.percentile(bootstrap_means, 97.5)
print(f"--- Нәтиже ---")
print(f"Түпнұсқа орта мән: {np.mean(data):.2f}")
print(f"Бутстреп орта мәні: {np.mean(bootstrap_means):.2f}")
print(f"95% сенімділік аралығы: [{lower_bound:.2f}, {upper_bound:.2f}]")
