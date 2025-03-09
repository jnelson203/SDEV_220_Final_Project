from inventory_management.inventory_item import InventoryItem

class Inventory:
    def __init__(self):
   
        self.items = []

    def add_item(self, item):

        if not isinstance(item, InventoryItem):
            raise ValueError("Only InventoryItem instances can be added.")
        self.items.append(item)

    def remove_item(self, item_name):

        self.items = [item for item in self.items if item.name != item_name]

    def update_item(self, item_name, new_quantity=None, new_price=None):
        
        for item in self.items:
            if item.name == item_name:
                if new_quantity is not None:
                    item.update_quantity(new_quantity)
                if new_price is not None:
                    item.update_price(new_price)
                break
        else:
            raise ValueError(f"Item with name '{item_name}' not found.")

    def list_items(self):

        return [(item.name, item.category, item.quantity, item.price) for item in self.items]

    def find_item(self, item_name):
  
        for item in self.items:
            if item.name == item_name:
                return item
        return None
