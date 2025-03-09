class InventoryItem:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity):
    
        self.quantity = new_quantity

    def update_price(self, new_price):

        self.price = new_price

    def __str__(self):
  
        return f"Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Price: ${self.price:.2f}"
