from models.transaction import Transaction
from models.transaction_manager import TransactionManager

manager = TransactionManager()

# create objects of class Transaction
t1 = Transaction(1000, "05-03-2025", "salary", "Monthly paycheck", "income")
t2 = Transaction(1000, "05-04-2025", "salary", "Monthly paycheck", "income")
t3 = Transaction(500, "05-05-2025", "transport", "Transport", "income")
t4 = Transaction(100, "21-03-2025", "groceries", "Food", "expense")
t5 = Transaction(100, "21-03-2025", "misc", "Gift", "expense")
t6 = Transaction(100, "05-04-2024", "groceries", "Food", "expense")
t7 = Transaction(100, "10-04-2025", "groceries", "Food", "expense")
t8 = Transaction(100, "06-05-2025", "misc", "Gift", "expense")
t9 = Transaction(100, "06-05-2024", "misc", "Gym", "expense")
t10 = Transaction(1000, "05-04-2024", "salary", "Monthly paycheck", "income")

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

print("\nTOTAL")
print(manager.get_total_income())
print(manager.get_total_expenses())
print(manager.get_net_worth())

print("\nNET WORTH BY MONTH AND YEAR")
print(manager.get_net_worth_by_month())
print(manager.get_net_worth_by_year())

print("\nSORTED NET WORTH BY MONTH AND YEAR")
print(manager.get_sorted_net_worth_by_month())
print(manager.get_sorted_net_worth_by_year())

print("\nBY CATEGORY")
print(manager.get_expenses_by_category())
print(manager.get_income_by_category())

print("\nEXPENSES BY DATE")
print(manager.get_expenses_by_date())

print("\nnEXPENSES BY DATE SORTED DESCENDING")
print(manager.get_sorted_expenses_by_date())

print("\nnEXPENSES BY DATE SORTED ASCENDING")
print(manager.get_sorted_expenses_by_date(False))

print("\nEXPENSES BY MONTH")
print(manager.get_expenses_by_month())

print("\nSORTED EXPENSES BY MONTH DESCENDING")
print(manager.get_sorted_expenses_by_month())

print("\nSORTED EXPENSES BY MONTH ASCENDING")
print(manager.get_sorted_expenses_by_month(False))

print("\nINCOME BY MONTH")
print(manager.get_income_by_month())

print("\nSORTED INCOME BY MONTH")
print(manager.get_sorted_income_by_month())

print("\nEXPENSES BY YEAR")
print(manager.get_expenses_by_year())

print("\nINCOME BY YEAR")
print(manager.get_income_by_year())

print("\nSORTED INCOME BY YEAR")
print(manager.get_sorted_income_by_year())
