import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Item class
class Item:
    def __init__(self, name, sku, category, description, barcode, quantity_on_hand, unit_cost, storage_location, supplier_name, supplier_contact, reorder_point, date_received, date_sold=None, expiration_date=None, lot_number=None):
        self.name = name
        self.sku = sku
        self.category = category
        self.description = description
        self.barcode = barcode
        self.quantity_on_hand = quantity_on_hand
        self.unit_cost = unit_cost
        self.total_cost = quantity_on_hand * unit_cost
        self.reorder_point = reorder_point
        self.storage_location = storage_location
        self.supplier_name = supplier_name
        self.supplier_contact = supplier_contact
        self.date_received = date_received
        self.date_sold = date_sold
        self.expiration_date = expiration_date
        self.lot_number = lot_number

    def update_total_cost(self):
        self.total_cost = self.quantity_on_hand * self.unit_cost

# Inventory class
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def search_items(self, search_term):
        return [item for item in self.items if search_term.lower() in item.name.lower() or search_term.lower() in item.category.lower() or search_term.lower() in item.description.lower()]

    def generate_report(self):
        return "\n".join([f"{item.name} - {item.sku} - {item.category} - {item.description} - {item.storage_location} - Quantity: {item.quantity_on_hand} - Total Cost: ${item.total_cost} - Reorder Point: {item.reorder_point} - Supplier: {item.supplier_name} ({item.supplier_contact})" for item in self.items])

# GUI class
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Goodwill Inventory Management System")
        self.root.geometry("800x600")
        self.root.config(bg="#E4F1F1")
        self.inventory = Inventory()

        # Adding items programmatically
        self.add_initial_items()

        self.create_widgets()

    def add_initial_items(self):
        item1 = Item(
            name="Wooden Chair",
            sku="CHAIR001",
            category="Furniture",
            description="Used wooden chair in good condition.",
            barcode="123456789012",
            quantity_on_hand=10,
            unit_cost=25.50,
            storage_location="Aisle 2",
            supplier_name="Home Furnishings Inc.",
            supplier_contact="123-456-7890",
            reorder_point=5,
            date_received=datetime.today().strftime('%Y-%m-%d'),
            expiration_date=None,
            lot_number=None
        )
        self.inventory.add_item(item1)

        item2 = Item(
            name="LED TV",
            sku="TV123",
            category="Electronics",
            description="42-inch LED TV with smart features.",
            barcode="987654321098",
            quantity_on_hand=5,
            unit_cost=300.00,
            storage_location="Aisle 4",
            supplier_name="Tech World",
            supplier_contact="987-654-3210",
            reorder_point=2,
            date_received=datetime.today().strftime('%Y-%m-%d'),
            expiration_date=None,
            lot_number=None
        )
        self.inventory.add_item(item2)

        item3 = Item(
            name="Leather Sofa",
            sku="SOFA456",
            category="Furniture",
            description="High-quality leather sofa with three seats.",
            barcode="543210987654",
            quantity_on_hand=3,
            unit_cost=450.00,
            storage_location="Aisle 1",
            supplier_name="Luxury Living",
            supplier_contact="321-654-9870",
            reorder_point=1,
            date_received=datetime.today().strftime('%Y-%m-%d'),
            expiration_date=None,
            lot_number=None
        )
        self.inventory.add_item(item3)

    def create_widgets(self):
        # Header label with modern font and color
        self.label = tk.Label(self.root, text="Goodwill Inventory Management", font=("Arial", 24, "bold"), bg="#4CAF50", fg="white", pady=20)
        self.label.pack(fill="x")
        
        # Main frame to organize the layout
        self.main_frame = tk.Frame(self.root, bg="#E4F1F1")
        self.main_frame.pack(pady=10)

        # Add Donation Button with modern style
        self.add_donation_button = tk.Button(self.main_frame, text="Add Donation", command=self.add_donation, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20, height=2, relief="flat", bd=0, padx=10, pady=10)
        self.add_donation_button.grid(row=0, column=0, padx=20, pady=10)

        # Search Label and Entry with cleaner look
        self.search_label = tk.Label(self.main_frame, text="Search by Name, Category, or Description:", bg="#E4F1F1", font=("Arial", 12), anchor="w")
        self.search_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        self.search_entry = tk.Entry(self.main_frame, font=("Arial", 12), width=20, relief="solid", bd=1)
        self.search_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Search Button with hover effect
        self.search_button = tk.Button(self.main_frame, text="Search Inventory", command=self.search_inventory, bg="#4CAF50", fg="white", font=("Arial", 12), width=20, height=2, relief="flat", bd=0, padx=10, pady=10)
        self.search_button.grid(row=1, column=2, padx=20, pady=10)

        # Generate Report Button with improved style
        self.generate_report_button = tk.Button(self.main_frame, text="Generate Report", command=self.generate_report, bg="#4CAF50", fg="white", font=("Arial", 12), width=20, height=2, relief="flat", bd=0, padx=10, pady=10)
        self.generate_report_button.grid(row=2, column=0, columnspan=3, pady=10)

    def add_donation(self):
        self.donation_window = tk.Toplevel(self.root)
        self.donation_window.title("Add Donation")
        self.donation_window.geometry("500x600")
        self.donation_window.config(bg="#E4F1F1")

        # Donation form fields with padding and neat design
        self.name_label = tk.Label(self.donation_window, text="Item Name:", bg="#E4F1F1", font=("Arial", 12))
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.donation_window, font=("Arial", 12), relief="solid", bd=1)
        self.name_entry.pack(pady=5)

        self.sku_label = tk.Label(self.donation_window, text="SKU:", bg="#E4F1F1", font=("Arial", 12))
        self.sku_label.pack(pady=5)
        self.sku_entry = tk.Entry(self.donation_window, font=("Arial", 12), relief="solid", bd=1)
        self.sku_entry.pack(pady=5)

        self.category_label = tk.Label(self.donation_window, text="Category:", bg="#E4F1F1", font=("Arial", 12))
        self.category_label.pack(pady=5)
        self.category_entry = tk.Entry(self.donation_window, font=("Arial", 12), relief="solid", bd=1)
        self.category_entry.pack(pady=5)

        self.description_label = tk.Label(self.donation_window, text="Description:", bg="#E4F1F1", font=("Arial", 12))
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(self.donation_window, font=("Arial", 12), relief="solid", bd=1)
        self.description_entry.pack(pady=5)

        self.quantity_label = tk.Label(self.donation_window, text="Quantity on Hand:", bg="#E4F1F1", font=("Arial", 12))
        self.quantity_label.pack(pady=5)
        self.quantity_entry = tk.Entry(self.donation_window, font=("Arial", 12), relief="solid", bd=1)
        self.quantity_entry.pack(pady=5)

        self.unit_cost_label = tk.Label(self.donation_window, text="Unit Cost ($):", bg="#E4F1F1", font=("Arial", 12))
        self.unit_cost_label.pack(pady=5)
        self.unit_cost_entry = tk.Entry(self.donation_window, font=("Arial", 12), relief="solid", bd=1)
        self.unit_cost_entry.pack(pady=5)

        self.date_received_label = tk.Label(self.donation_window, text="Date Received:", bg="#E4F1F1", font=("Arial", 12))
        self.date_received_label.pack(pady=5)
        self.date_received_entry = tk.Entry(self.donation_window, font=("Arial", 12), relief="solid", bd=1)
        self.date_received_entry.pack(pady=5)
        self.date_received_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        # Add item button with modern style
        self.add_item_button = tk.Button(self.donation_window, text="Add Item", command=self.add_item_to_inventory, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20, height=2, relief="flat", bd=0, padx=10, pady=10)
        self.add_item_button.pack(pady=20)

    def add_item_to_inventory(self):
        name = self.name_entry.get()
        sku = self.sku_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        barcode = self.barcode_entry.get()
        quantity_on_hand = int(self.quantity_entry.get())
        unit_cost = float(self.unit_cost_entry.get())
        storage_location = self.storage_location_entry.get()
        supplier_name = self.supplier_name_entry.get()
        supplier_contact = self.supplier_contact_entry.get()
        reorder_point = int(self.reorder_point_entry.get())
        date_received = self.date_received_entry.get()

        new_item = Item(name, sku, category, description, barcode, quantity_on_hand, unit_cost, storage_location, supplier_name, supplier_contact, reorder_point, date_received)
        self.inventory.add_item(new_item)

        messagebox.showinfo("Success", f"Item '{name}' added to inventory!")
        self.donation_window.destroy()

    def search_inventory(self):
        search_term = self.search_entry.get()
        found_items = self.inventory.search_items(search_term)

        if found_items:
            result_str = "\n".join([f"{item.name} - {item.sku} - {item.category} - {item.description}" for item in found_items])
            messagebox.showinfo("Search Results", result_str)
        else:
            messagebox.showinfo("Search Results", "No items found!")

    def generate_report(self):
        report = self.inventory.generate_report()
        messagebox.showinfo("Inventory Report", report)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

