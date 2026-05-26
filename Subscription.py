import pandas as pd


class Subscription:
    def __init__(self, user: str, plan: str, amount: float, paid: bool):
        if amount <= 0:
            raise ValueError(f"Қате: {user} үшін сома 0-ден үлкен болуы керек!")
        if not user or not plan:
            raise ValueError("Қате: Қолданушы аты немесе тариф бос болмауы керек!")
        self.user = user
        self.plan = plan
        self.amount = float(amount)
        self.paid = bool(paid)

    def display_info(self):
        status = "Төленген" if self.paid else "Төленбеген"
        return f"Қолданушы: {self.user} | Тариф: {self.plan} | Сома: {self.amount} теңге | Статус: {status}"

df = pd.read_csv("subscriptions.csv")

for index, row in df.iterrows():
    try:
        sub = Subscription(
            row["user"],
            row["plan"],
            row["amount"],
            row["paid"]
        )

        print(sub.display_info())

    except ValueError as e:
        print(e)