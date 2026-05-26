import pandas as pd
import numpy as np
import os


class Bootstrapper_12:

    def __init__(self, file=None, B=500):

        self.B = B

        if file and os.path.exists(file):
            df = pd.read_csv(file)
            self.data = df.iloc[:, 0].dropna().values
            print("CSV файл оқылды!")
        else:
            print("CSV табылмады → random data жасалды!")
            self.data = np.random.randint(10, 100, 50)

        if len(self.data) == 0:
            raise ValueError("Деректер бос!")

        print("Data size:", len(self.data))

    def run(self):

        means = []
        rng = np.random.default_rng()

        for _ in range(self.B):
            sample = rng.choice(self.data, size=len(self.data), replace=True)
            means.append(np.mean(sample))

        means = np.array(means)

        result = pd.DataFrame({
            "mean": [np.mean(self.data)],
            "lo": [np.percentile(means, 2.5)],
            "hi": [np.percentile(means, 97.5)]
        })

        result.to_csv("bootstrap_summary.csv", index=False)

        print("\nRESULT:")
        print(result)
        print("\nbootstrap_summary.csv сақталды!")


model = Bootstrapper_12(file="sample.csv", B=1000)
model.run()