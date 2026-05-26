import json
import pandas as pd


class BillingReporter:
    def __init__(self, data_list):
        self.data = data_list

    def unpaid_generator(self):
        """7. Төленбеген жазылымдарды қайтаратын генератор"""
        for item in self.data:
            if not item['paid']:
                yield item

    def export_to_json(self, filename="report.json"):

        """8. Мәліметтерді JSON форматында файлға жазу"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

        print(f"Есеп сәтті сақталды: {filename}")


# CSV файл оқу
df = pd.read_csv("subscriptions3")

# DataFrame → list түріне ауыстыру
test_data = df.to_dict(orient="records")


reporter = BillingReporter(test_data)

print("Генератор арқылы төленбегендерді шығару:")

for unpaid in reporter.unpaid_generator():
    print(f"- {unpaid['user']} қарызы бар.")


reporter.export_to_json()