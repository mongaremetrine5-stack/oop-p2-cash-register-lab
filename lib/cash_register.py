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

    # Add an item to the register
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

    # Apply discount to total
  def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self.total = self.total * (1 - self.discount / 100)
        # Remove last transaction
        last_transaction = self.previous_transactions.pop()
        # Remove items from the items list
        for _ in range(last_transaction["quantity"]):
            self.items.pop()

    # Void the last transaction
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

