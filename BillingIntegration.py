import matplotlib.pyplot as plt
import requests
import pandas as pd


class BillingIntegration:
    def __init__(self, plans_list, mrr_values, all_data):
        self.plans = plans_list
        self.mrr = mrr_values
        self.all_data = all_data
    def plot_mrr_chart(self):

        plt.figure(figsize=(6, 4))
        plt.bar(self.plans, self.mrr)
        plt.title('Тарифтер бойынша MRR табысы')
        plt.xlabel('Тариф түрі')
        plt.ylabel('Сома (теңге)')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()
    def sync_with_api(self):

        url = "https://httpbin.org/post"

        print("\nAPI-ға сұраныс жіберілуде...")

        try:
            response = requests.post(
                url,
                json=self.all_data
            )

            if response.status_code == 200:
                print("Сұраныс сәтті! Биллинг API мәліметтерді қабылдады.")

        except Exception as e:
            print(f"API қатесі: {e}")


# CSV оқу
df = pd.read_csv("subscriptions5.csv")

# Бағандарды тізімге айналдыру
plans = df["plan"].tolist()
mrr_vals = df["mrr"].tolist()

# API-ға жіберілетін мәлімет
data_to_send = {
    "batch_id": 101,
    "status": "processed"
}

integration = BillingIntegration(
    plans,
    mrr_vals,
    data_to_send
)

integration.sync_with_api()
integration.plot_mrr_chart()