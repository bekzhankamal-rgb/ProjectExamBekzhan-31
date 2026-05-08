import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class BootstrapAnalyzer:

    def __init__(self, B=500):
        self.B = B

    def load_data(self):
        user_input = input("Сандарды енгіз (үтірмен бөл): ")

        values = np.array([
            float(x.strip()) for x in user_input.split(",")
        ])

        return values

    def bootstrap(self):
        values = self.load_data()

        rng = np.random.default_rng()

        means = []

        for _ in range(self.B):
            sample = rng.choice(
                values,
                size=len(values),
                replace=True
            )
            means.append(sample.mean())

        means = np.array(means)

        original_mean = values.mean()
        lo = np.percentile(means, 2.5)
        hi = np.percentile(means, 97.5)

        result = pd.DataFrame([{
            "mean": original_mean,
            "lo": lo,
            "hi": hi
        }])

        print(result)

        plt.figure(figsize=(8, 5))
        plt.hist(means, bins=30)

        plt.axvline(lo, linestyle="--", label="2.5%")
        plt.axvline(hi, linestyle="--", label="97.5%")

        plt.title("Bootstrap Means")
        plt.xlabel("Mean")
        plt.ylabel("Count")
        plt.legend()

        plt.show()


analyzer = BootstrapAnalyzer(B=500)
analyzer.bootstrap()