class CashRegister:
    def __init__(self):
        self.total = 0 
        self.discount = 0  
        self.items = []  
        self.last_transaction = 0  

    def add_item(self, item_price):
       
        self.total += item_price
       
        self.last_transaction = item_price
       
        self.items.append(item_price)

    
    def apply_discount(self):
     
        if self.discount > 0:
            
            discount_amount = (self.discount / 100) * self.total
        
            self.total -= discount_amount
           
            self.total = int(self.total)
            return f"Discount applied: {self.discount}% off. New total: ${self.total}"
        else:
            return "No discount to apply."

    def void_last_transaction(self):
        if self.last_transaction > 0:
           
            self.total -= self.last_transaction
            
            self.items.pop()
          
            self.last_transaction = 0
        else:
            return "No transactions to void."


register = CashRegister()
register.add_item(10)
register.add_item(20)
register.discount = 10  
discount_message = register.apply_discount()
print(discount_message)  
print(register.total)  


register.apply_discount() 
register.apply_discount(10)
print(register.total)  

register.void_last_transaction()
print(register.total)  