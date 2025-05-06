from models.transaction import Transaction
import json


class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def list_transactions(self):
        for num, transaction in enumerate(self.transactions, start=1):
            print(
                f"{num}. {transaction.date} - {transaction.type} - {transaction.amount} - {transaction.category} ({transaction.description})"
            )

    # SAVING AND LOADING TO A JSON FILE

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            data = [transaction.to_dict() for transaction in self.transactions]
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(item) for item in data]
        except FileNotFoundError:
            print(f"No file found at {filename}. Starting with an empty list.")
            self.transactions = []

    # CALCULATIONS FOR EXPENSES

    def get_total_expenses(self):
        total = 0
        for t in self.transactions:
            if t.type == "expense":
                total += t.amount
        return total

    def get_expenses_by_category(self):
        total_by_category = {}
        for t in self.transactions:
            if t.type == "expense":
                if t.category not in total_by_category:
                    total_by_category[t.category] = 0
                total_by_category[t.category] += t.amount
        return total_by_category

    def get_expenses_by_date(self):
        total_by_date = {}
        for t in self.transactions:
            if t.type == "expense":
                if t.date not in total_by_date:
                    total_by_date[t.date] = 0
                total_by_date[t.date] += t.amount
        return total_by_date

    def get_expenses_by_month(self):
        total_by_month = {}
        for t in self.transactions:
            if t.type == "expense":
                month = t.date[:7]
                if month not in total_by_month:
                    total_by_month[month] = 0
                total_by_month[month] += t.amount
        return total_by_month

    def get_expenses_by_year(self):
        total_by_year = {}
        for t in self.transactions:
            if t.type == "expense":
                year = t.date[:4]
                if year not in total_by_year:
                    total_by_year[year] = 0
                total_by_year[year] += t.amount
        return total_by_year

    # CALCULATIONS FOR INCOME

    def get_total_income(self):
        total = 0
        for t in self.transactions:
            if t.type == "income":
                total += t.amount
        return total

    def get_income_by_category(self):
        total_by_category = {}
        for t in self.transactions:
            if t.type == "income":
                if t.category not in total_by_category:
                    total_by_category[t.category] = 0
                total_by_category[t.category] += t.amount
        return total_by_category

    def get_income_by_month(self):
        total_by_month = {}
        for t in self.transactions:
            if t.type == "income":
                month = t.date[:7]
                if month not in total_by_month:
                    total_by_month[month] = 0
                total_by_month[month] += t.amount
        return total_by_month

    def get_income_by_year(self):
        total_by_year = {}
        for t in self.transactions:
            if t.type == "income":
                year = t.date[:4]
                if year not in total_by_year:
                    total_by_year[year] = 0
                total_by_year[year] += t.amount
        return total_by_year

    # CALCULATIONS FOR NET WORTH

    def get_net_worth(self):
        return self.get_total_income() + self.get_total_expenses()

    def get_net_worth_by_month(self):
        net_worth_by_month = {}
        total_income_by_month = self.get_income_by_month()
        total_expenses_by_month = self.get_expenses_by_month()
        net_worth_by_month.update(
            self.merge_dicts(total_income_by_month, total_expenses_by_month)
        )
        return net_worth_by_month

    def get_net_worth_by_year(self):
        net_worth_by_year = {}
        total_income_by_year = self.get_income_by_year()
        total_expenses_by_year = self.get_expenses_by_year()
        net_worth_by_year.update(
            self.merge_dicts(total_income_by_year, total_expenses_by_year)
        )
        return net_worth_by_year

    # HELPER FUNCTIONS

    def merge_dicts(self, dict1, dict2):
        merged_dict = {}

        for key in dict1:
            if key in dict2:
                new_value = dict1[key] + dict2[key]
            else:
                new_value = dict1[key]

            merged_dict[key] = new_value

        for key in dict2:
            if key not in merged_dict:
                merged_dict[key] = dict2[key]

        return merged_dict
