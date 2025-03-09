import csv
from inventory_management.inventory import Inventory

class ReportGenerator:
    def __init__(self, inventory):
  
        self.inventory = inventory

    def generate_report(self, filename="inventory_report.csv"):
   
        # Create a list of headers for the CSV
        headers = ['Name', 'Category', 'Quantity', 'Price']
        
        # Open the file in write mode
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(headers)
            
            # Write the inventory items
            for item in self.inventory.items:
                writer.writerow([item.name, item.category, item.quantity, item.price])
        
        print(f"Report generated successfully: {filename}")

    def generate_summary(self):

        total_items = 0
        total_value = 0.0
        
        # Iterate through the items and calculate the total number and value
        for item in self.inventory.items:
            total_items += item.quantity
            total_value += item.quantity * item.price
        
        # Create a summary dictionary
        summary = {
            "total_items": total_items,
            "total_value": total_value
        }
        
        return summary

    def display_summary(self):
   
        summary = self.generate_summary()
        
        print("Inventory Summary:")
        print(f"Total number of items: {summary['total_items']}")
        print(f"Total inventory value: ${summary['total_value']:.2f}")
