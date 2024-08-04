#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, total, quantity=1):
        self.total += total * quantity
        for i in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": total}
        )

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        self.total -= (
            self.previous_transactions[-1]["price"]
            * self.previous_transactions[-1]["quantity"]
        )
        for i in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()
            self.previous_transactions.pop()
    

    
