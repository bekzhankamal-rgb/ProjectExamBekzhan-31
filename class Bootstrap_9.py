import pandas as pd
import numpy as np

class Bootstrap_9:
    def __init__(self, file):
        self.data = pd.read_csv(file).values.flatten()
    def calculate(self, B=500):
        rng = np.random.default_rng()
        means = [np.mean(rng.choice(self.data, size=len(self.data), replace=True)) for _ in range(B)]
        print(f"2.5%: {np.percentile(means, 2.5)}")
        print(f"97.5%: {np.percentile(means, 97.5)}")

bt = Bootstrap_9('../sample.csv')
bt.calculate()