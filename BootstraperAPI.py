from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()


class BootstraperAPI:
    def __init__(self, B=500):
        self.B = B
        self.rng = np.random.default_rng()

    def bootstrap(self, data):
        values = np.array(data)

        boot_means = [
            self.rng.choice(values, size=len(values), replace=True).mean()
            for _ in range(self.B)
        ]

        boot_means = np.array(boot_means)

        return {
            "mean": float(values.mean()),
            "lo": float(np.percentile(boot_means, 2.5)),
            "hi": float(np.percentile(boot_means, 97.5))
        }


# ---------------- FASTAPI PART ----------------

class RequestModel(BaseModel):
    numbers: list[float]


api = BootstraperAPI()


@app.post("/bootstrap")
def run_bootstrap(req: RequestModel):
    return api.bootstrap(req.numbers)