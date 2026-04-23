import pandas as pd
import numpy as np


class Bootstrapper_11:
    def __init__(self, data):
        self.df = pd.Series(data).dropna()

        if self.df.empty:
            raise ValueError("Деректер бос!")

    def run(self, B=1000):
        means = [
            self.df.sample(len(self.df), replace=True).mean()
            for _ in range(B)
        ]

        res = pd.Series(means)

        return pd.DataFrame({
            'Original_Mean': [self.df.mean()],
            'Low_2.5%': [res.quantile(0.025)],
            'High_97.5%': [res.quantile(0.975)]
        })


np.random.seed(42)
data = np.random.normal(50, 10, 100)

analyzer = Bootstrapper_11(data)
print(analyzer.run())