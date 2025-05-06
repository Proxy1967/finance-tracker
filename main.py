from models.transaction import Transaction
from models.transaction_manager import TransactionManager

manager = TransactionManager()

# create objects of class Transaction
t1 = Transaction(1000, "2025-03-05", "salary", "Monthly paycheck", "income")
t2 = Transaction(1000, "2025-04-05", "salary", "Monthly paycheck", "income")
t3 = Transaction(500, "2025-05-05", "transport", "Transport", "income")
t4 = Transaction(100, "2025-03-21", "groceries", "Food", "expense")
t5 = Transaction(100, "2025-03-21", "misc", "Gift", "expense")
t6 = Transaction(100, "2025-04-05", "groceries", "Food", "expense")
t7 = Transaction(100, "2025-04-10", "groceries", "Food", "expense")
t8 = Transaction(100, "2025-05-06", "misc", "Gift", "expense")
t9 = Transaction(100, "2024-05-06", "misc", "Gym", "expense")
t10 = Transaction(1000, "2024-04-05", "salary", "Monthly paycheck", "income")

# data = t1.to_dict()
# transaction = Transaction.from_dict(data)
# print(transaction.amount)

# add transactions to a list
manager.add_transaction(t1)
manager.add_transaction(t2)
manager.add_transaction(t3)
manager.add_transaction(t4)
manager.add_transaction(t5)
manager.add_transaction(t6)
manager.add_transaction(t7)
manager.add_transaction(t8)
manager.add_transaction(t9)
manager.add_transaction(t10)

# save the transactions to a json file
manager.save_to_file("data/transactions.json")

manager.load_from_file("data/transactions.json")

manager.list_transactions()

print("")
print(manager.get_total_income())
print(manager.get_total_expenses())
print(manager.get_net_worth())
print(manager.get_net_worth_by_month())
print(manager.get_net_worth_by_year())
print("")
print(manager.get_expenses_by_category())
print(manager.get_income_by_category())
print("")
print(manager.get_expenses_by_date())
print("")
print(manager.get_expenses_by_month())
print(manager.get_income_by_month())
print("")
print(manager.get_expenses_by_year())
print(manager.get_income_by_year())
