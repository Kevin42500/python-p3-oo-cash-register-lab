class CashRegister:
    def __init__(self):
        self.total = 0  # Initialize the total price to zero
        self.discount = 0  # Initialize the discount to zero
        self.items = []  # Initialize an empty list to store items
        self.last_transaction = 0  # Initialize the last_transaction to zero

    def add_item(self, item_price):
        # Add the item price to the total
        self.total += item_price
        # Store the item price in the last_transaction attribute
        self.last_transaction = item_price
        # Append the item price to the list of items
        self.items.append(item_price)

    
    def apply_discount(self):
        # Check if a discount is available
        if self.discount > 0:
            # Calculate the discount amount
            discount_amount = (self.discount / 100) * self.total
            # Apply the discount to the total
            self.total -= discount_amount
            # Convert the total to an integer (rounding it)
            self.total = int(self.total)
            return f"Discount applied: {self.discount}% off. New total: ${self.total}"
        else:
            return "No discount to apply."

    def void_last_transaction(self):
        if self.last_transaction > 0:
            # Subtract the last transaction amount from the total
            self.total -= self.last_transaction
            # Remove the last item from the list of items
            self.items.pop()
            # Set last_transaction to zero
            self.last_transaction = 0
        else:
            return "No transactions to void."

# Example usage:
register = CashRegister()
register.add_item(10)
register.add_item(20)
register.discount = 10  # Set the discount to 10%
discount_message = register.apply_discount()
print(discount_message)  # Output: "Discount applied: 10% off. New total: $27"
print(register.total)  # Output: 27


register.apply_discount()  # Output: "No discount to apply."

register.apply_discount(10)
print(register.total)  # Output: 27

register.void_last_transaction()
print(register.total)  # Output: 10
