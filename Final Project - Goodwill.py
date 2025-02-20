import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import threading

# Database Setup
def initialize_db():
    conn = sqlite3.connect("goodwill_inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category_id INTEGER,
            condition TEXT,
            date_received TEXT,
            location_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES Categories(id),
            FOREIGN KEY (location_id) REFERENCES Locations(id)
        )
    """)
    conn.commit()
    conn.close()

# Function to add donations
def add_donation():
    name = entry_name.get()
    category = combo_category.get()
    condition = combo_condition.get()
    date_received = entry_date.get()
    location = combo_location.get()
    
    if not (name and category and condition and date_received and location):
        messagebox.showerror("Input Error", "All fields are required")
        return
    
    conn = sqlite3.connect("goodwill_inventory.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT OR IGNORE INTO Categories (name) VALUES (?)", (category,))
    cursor.execute("INSERT OR IGNORE INTO Locations (name) VALUES (?)", (location,))
    
    cursor.execute("SELECT id FROM Categories WHERE name = ?", (category,))
    category_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM Locations WHERE name = ?", (location,))
    location_id = cursor.fetchone()[0]
    
    cursor.execute("""
        INSERT INTO Donations (name, category_id, condition, date_received, location_id)
        VALUES (?, ?, ?, ?, ?)
    """, (name, category_id, condition, date_received, location_id))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Donation added successfully!")
    display_donations()

# Function to display donations using threading
def display_donations():
    def fetch_data():
        conn = sqlite3.connect("goodwill_inventory.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Donations.name, Categories.name, Donations.condition, Donations.date_received, Locations.name
            FROM Donations
            JOIN Categories ON Donations.category_id = Categories.id
            JOIN Locations ON Donations.location_id = Locations.id
        """)
        rows = cursor.fetchall()
        conn.close()
        
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    
    threading.Thread(target=fetch_data).start()

# GUI Setup
root = tk.Tk()
root.title("Goodwill Inventory Management")
root.geometry("700x500")

# Input Fields
frame = ttk.Frame(root, padding=10)
frame.pack(pady=10)

ttk.Label(frame, text="Item Name:").grid(row=0, column=0)
entry_name = ttk.Entry(frame)
entry_name.grid(row=0, column=1)

categories = ["Clothing", "Furniture", "Electronics"]
ttk.Label(frame, text="Category:").grid(row=1, column=0)
combo_category = ttk.Combobox(frame, values=categories)
combo_category.grid(row=1, column=1)

conditions = ["New", "Good", "Fair", "Poor"]
ttk.Label(frame, text="Condition:").grid(row=2, column=0)
combo_condition = ttk.Combobox(frame, values=conditions)
combo_condition.grid(row=2, column=1)

locations = ["Store A", "Store B", "Warehouse"]
ttk.Label(frame, text="Location:").grid(row=3, column=0)
combo_location = ttk.Combobox(frame, values=locations)
combo_location.grid(row=3, column=1)

ttk.Label(frame, text="Date Received:").grid(row=4, column=0)
entry_date = ttk.Entry(frame)
entry_date.grid(row=4, column=1)

# Buttons
ttk.Button(frame, text="Add Donation", command=add_donation).grid(row=5, columnspan=2, pady=10)

# Display Table
tree = ttk.Treeview(root, columns=("Name", "Category", "Condition", "Date Received", "Location"), show="headings")
for col in ("Name", "Category", "Condition", "Date Received", "Location"):
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(pady=10)

display_donations()
initialize_db()
root.mainloop()
