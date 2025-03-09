from inventory_management.inventory import Inventory
from inventory_management.gui import InventoryApp
import tkinter as tk

def main():
    # Initialize the inventory system
    inventory = Inventory()

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Goodwill Inventory Management")

    # Initialize the InventoryApp with the root window and inventory system
    app = InventoryApp(root, inventory)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
