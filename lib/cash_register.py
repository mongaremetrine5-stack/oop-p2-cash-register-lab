#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Validate discount
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        # Track transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Check if any transactions exist
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return  # Exit early

        # Apply discount if there are transactions
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${int(self.total)}.")
    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        # Subtract from total
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        # Remove items from items list
        for _ in range(last_transaction["quantity"]):
            self.items.pop()

