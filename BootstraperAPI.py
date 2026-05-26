import numpy as np
import pandas as pd
import requests
import os

class BootstraperAPI:
    def __init__(self, file=None, B=500, seed=None):
        self.B = B
        self.rng = np.random.default_rng(seed)

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
        self.summary = None

    def run(self):

        means = np.array([
            self.rng.choice(self.data, size=len(self.data), replace=True).mean()
            for _ in range(self.B)
        ])


        self.summary = pd.DataFrame([{
            "mean": np.mean(self.data),
            "lo": np.percentile(means, 2.5),
            "hi": np.percentile(means, 97.5)
        }])

        self.summary.to_csv("bootstrap_summary.csv", index=False)
        print("\nRESULT:")
        print(self.summary)
        print("\nbootstrap_summary.csv сақталды!")

    def post_json(self, url):

        if self.summary is None:
            raise ValueError("Алдымен run() шақыру керек.")
        payload = self.summary.iloc[0].to_dict()
        response = requests.post(url, json=payload)
        print("\nPOST status:", response.status_code)
        print("Response:", response.text)
        return response


api = BootstraperAPI(file="sample.csv", B=500)
api.run()
url = "http://example.com/api/bootstrap"
api.post_json(url)
