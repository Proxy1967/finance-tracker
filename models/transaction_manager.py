from models.transaction import Transaction
import json

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def list_transactions(self):
        for num, transaction in enumerate(self.transactions, start=1):
            print(f"{num}. {transaction.date} - {transaction.type} - €{transaction.amount} - {transaction.category} - {transaction.description}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            data = [transaction.to_dict() for transaction in self.transactions]
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(item) for item in data]
        except FileNotFoundError:
            print(f"No file found at {filename}. Starting with an empty list.")
            self.transactions = []