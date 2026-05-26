import pandas as pd


class SubscriptionBilling:
    def __init__(self):
        # Жазылымдар тізімі
        self.subscriptions = []

    def add_subscription(self, user, plan, amount, paid):
        """Жазылымдарды тізімге қосатын функция"""
        if amount > 0:
            new_sub = {
                "user": user,
                "plan": plan,
                "amount": amount,
                "paid": paid
            }

            self.subscriptions.append(new_sub)
            print(f"Жазылым қосылды: {user}")

        else:
            print("Қате: Төлем сомасы дұрыс емес.")

    def check_status(self, user):
        """Қолданушының төлем статусын тексеретін функция"""
        for sub in self.subscriptions:
            if sub['user'] == user:
                return f"{user} статусы: {'Төленген' if sub['paid'] else 'Төленбеген'}"

        return f"{user} табылмады."


# CSV файл оқу
df = pd.read_csv("subscriptionBilling")

billing_manager = SubscriptionBilling()

# Файлдағы мәліметтерді жүктеу
for index, row in df.iterrows():

    billing_manager.add_subscription(
        row["user"],
        row["plan"],
        row["amount"],
        row["paid"]
    )


# Тексеру
print(billing_manager.check_status("Berik"))