class Transaction:
    def __init__(self, amount, date, category, description, type):
        if type == "expense":
            self.amount = -abs(amount)
        else:
            self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.type = type

    def to_dict(self):
        return {
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "type": self.type,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data["amount"],
            date=data["date"],
            category=data["category"],
            description=data["description"],
            type=data["type"],
        )
