import pandas as pd
import numpy as np


class Bootstrapper_12:
    def __init__(self, file):
        self.data = pd.read_csv(file).iloc[:, 0].dropna().values

        if len(self.data) == 0:
            raise ValueError("Деректер бос!")

    def run(self):
        means = []

        for _ in range(1000):
            sample = np.random.choice(self.data, len(self.data), replace=True)
            means.append(np.mean(sample))

        res = pd.DataFrame({
            'mean': [np.mean(means)],
            'lo': [np.percentile(means, 2.5)],
            'hi': [np.percentile(means, 97.5)]
        })

        res.to_csv('bootstrap_summary.csv', index=False)
        print("Орындалды!")


model = Bootstrapper_12('sample.csv')
model.run()