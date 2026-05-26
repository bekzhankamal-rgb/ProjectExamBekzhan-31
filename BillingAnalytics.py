import pandas as pd


class BillingAnalytics:
    def __init__(self, raw_data):
        # Мәліметтерді DataFrame-ге айналдыру
        self.df = pd.DataFrame(raw_data)

    def get_mrr_by_plan(self):
        """9-12: Тек төленгендерді алып, groupby(plan) арқылы MRR есептеу"""

        # Тек төленген жазылымдарды сүзу
        paid_only = self.df[self.df['paid'] == True]

        # Тариф бойынша топтау
        mrr_df = paid_only.groupby('plan')['amount'].sum().reset_index()

        mrr_df.columns = ['Тариф (Plan)', 'MRR (Табыс)']

        return mrr_df


# CSV файл оқу
df = pd.read_csv("subscriptions4.csv")

# DataFrame → list
mrr_data = df.to_dict(orient="records")

analytics = BillingAnalytics(mrr_data)

mrr_result = analytics.get_mrr_by_plan()

print(mrr_result)