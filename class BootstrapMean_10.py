import numpy as np

class BootstrapMean_10:
    def __init__(self, data, B=500):
        self.data = np.array(data)
        self.B = B

    def run(self):
        self.means = [
            np.mean(np.random.choice(self.data, len(self.data), replace=True))
            for _ in range(self.B)
        ]
        return np.percentile(self.means, [2.5, 97.5])


# Тест деректер
data = np.random.normal(50, 10, 100)

bs = BootstrapMean_10(data)
interval = bs.run()

print(f"Сенімділік аралығы: {interval}")