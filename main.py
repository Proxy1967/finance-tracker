from models.transaction import Transaction
from models.transaction_manager import TransactionManager

manager = TransactionManager()

# # create objects of class Transaction
# t1 = Transaction(100, "2025-05-05", "salary", "Monthly paycheck", "income")
# t2 = Transaction(50, "2025-05-06", "groceries", "Food", "expense")

# # data = t1.to_dict()
# # transaction = Transaction.from_dict(data)
# # print(transaction.amount)

# # add transactions to a list
# manager.add_transaction(t1)
# manager.add_transaction(t2)

# # save the transactions to a json file
# manager.save_to_file("data/transactions.json")

manager.load_from_file("data/transactions.json")

manager.list_transactions()