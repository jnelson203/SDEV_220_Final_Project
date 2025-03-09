import tkinter as tk
from tkinter import messagebox
from inventory_management.inventory import Inventory
from inventory_management.inventory_item import InventoryItem
from inventory_management.report_generator import ReportGenerator

class InventoryGUI:
    def __init__(self, root, inventory):
 
        self.root = root
        self.inventory = inventory
        self.root.title("Goodwill Inventory Management")
        
        # Set window size
        self.root.geometry("600x400")
        
        # Create and place the widgets
        self.create_widgets()

    def create_widgets(self):
        """Create and place all the necessary widgets in the window."""
        # Title Label
        self.title_label = tk.Label(self.root, text="Goodwill Inventory Management", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Listbox to display items
        self.item_listbox = tk.Listbox(self.root, width=50, height=10)
        self.item_listbox.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.pack(side="left", padx=10)

        self.remove_button = tk.Button(self.root, text="Remove Item", command=self.remove_item)
        self.remove_button.pack(side="left", padx=10)

        self.update_button = tk.Button(self.root, text="Update Item", command=self.update_item)
        self.update_button.pack(side="left", padx=10)

        self.generate_report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.generate_report_button.pack(side="left", padx=10)

        self.view_summary_button = tk.Button(self.root, text="View Summary", command=self.view_summary)
        self.view_summary_button.pack(side="left", padx=10)

        # Populate the listbox with items
        self.update_listbox()

    def update_listbox(self):
        """Updates the listbox with the current items in the inventory."""
        self.item_listbox.delete(0, tk.END)
        for item in self.inventory.items:
            self.item_listbox.insert(tk.END, f"{item.name} - {item.category} - {item.quantity} - ${item.price:.2f}")

    def add_item(self):
        """Prompts the user to add a new item to the inventory."""
        # Open a new window for adding an item
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Item")
        
        # Labels and Entries for item details
        tk.Label(self.add_window, text="Item Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.add_window)
        self.name_entry.pack(pady=5)

        tk.Label(self.add_window, text="Category:").pack(pady=5)
        self.category_entry = tk.Entry(self.add_window)
        self.category_entry.pack(pady=5)

        tk.Label(self.add_window, text="Quantity:").pack(pady=5)
        self.quantity_entry = tk.Entry(self.add_window)
        self.quantity_entry.pack(pady=5)

        tk.Label(self.add_window, text="Price:").pack(pady=5)
        self.price_entry = tk.Entry(self.add_window)
        self.price_entry.pack(pady=5)

        # Button to save the new item
        self.save_button = tk.Button(self.add_window, text="Save Item", command=self.save_item)
        self.save_button.pack(pady=10)

    def save_item(self):
        """Saves the new item to the inventory."""
        name = self.name_entry.get()
        category = self.category_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values for quantity and price.")
            return
        
        # Add the item to the inventory
        new_item = InventoryItem(name, category, quantity, price)
        self.inventory.add_item(new_item)

        # Close the add item window and update the listbox
        self.add_window.destroy()
        self.update_listbox()

    def remove_item(self):
        """Removes the selected item from the inventory."""
        try:
            selected_item = self.item_listbox.get(self.item_listbox.curselection())
            item_name = selected_item.split(" - ")[0]
            self.inventory.remove_item(item_name)
            self.update_listbox()
        except tk.TclError:
            messagebox.showerror("Selection Error", "Please select an item to remove.")

    def update_item(self):
        """Prompts the user to update the selected item's details."""
        try:
            selected_item = self.item_listbox.get(self.item_listbox.curselection())
            item_name = selected_item.split(" - ")[0]
            item = self.inventory.find_item(item_name)

            # Open a new window for updating the item
            self.update_window = tk.Toplevel(self.root)
            self.update_window.title(f"Update {item_name}")

            # Labels and Entries for updated item details
            tk.Label(self.update_window, text="New Quantity:").pack(pady=5)
            self.new_quantity_entry = tk.Entry(self.update_window)
            self.new_quantity_entry.pack(pady=5)

            tk.Label(self.update_window, text="New Price:").pack(pady=5)
            self.new_price_entry = tk.Entry(self.update_window)
            self.new_price_entry.pack(pady=5)

            # Button to save the updated item
            self.save_update_button = tk.Button(self.update_window, text="Save Changes", command=lambda: self.save_update(item_name))
            self.save_update_button.pack(pady=10)
        except tk.TclError:
            messagebox.showerror("Selection Error", "Please select an item to update.")

    def save_update(self, item_name):
        """Saves the updated item details."""
        try:
            new_quantity = int(self.new_quantity_entry.get())
            new_price = float(self.new_price_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values for quantity and price.")
            return
        
        # Update the item in the inventory
        self.inventory.update_item(item_name, new_quantity, new_price)

        # Close the update window and refresh the listbox
        self.update_window.destroy()
        self.update_listbox()

    def generate_report(self):
        """Generates and saves a CSV report of the inventory."""
        report_generator = ReportGenerator(self.inventory)
        report_generator.generate_report()

    def view_summary(self):
        """Displays the inventory summary."""
        report_generator = ReportGenerator(self.inventory)
        summary = report_generator.generate_summary()

        # Show the summary in a messagebox
        summary_text = f"Total number of items: {summary['total_items']}\n"
        summary_text += f"Total inventory value: ${summary['total_value']:.2f}"

        messagebox.showinfo("Inventory Summary", summary_text)


# Main function to run the application
def main():
    # Create the root window
    root = tk.Tk()
    
    # Create an inventory instance
    inventory = Inventory()

    # Create the GUI and pass the inventory to it
    gui = InventoryGUI(root, inventory)
    
    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
