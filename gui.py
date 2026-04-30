import tkinter as tk
from tkinter import messagebox
from database import *

create_table()

selected_id = None

# ---------------- FUNCTIONS ---------------- #

def clear_fields():
    item_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)
    loc_entry.delete(0, tk.END)

def add_record():
    name = item_entry.get()
    qty = qty_entry.get()
    loc = loc_entry.get()

    if not name or not qty:
        messagebox.showerror("Error", "Fill all required fields")
        return

    insert_record(name, int(qty), loc)
    view_records()
    clear_fields()

def view_records():
    listbox.delete(0, tk.END)
    for row in get_all_records():
        listbox.insert(tk.END, f"ID:{row[0]} | {row[1]} | Qty:{row[2]} | {row[3]}")

def on_select(event):
    global selected_id

    if not listbox.curselection():
        return

    index = listbox.curselection()[0]
    text = listbox.get(index)

    parts = text.split("|")
    selected_id = int(parts[0].replace("ID:", "").strip())

    item_entry.delete(0, tk.END)
    item_entry.insert(0, parts[1].strip())

    qty_entry.delete(0, tk.END)
    qty_entry.insert(0, parts[2].replace("Qty:", "").strip())

    loc_entry.delete(0, tk.END)
    loc_entry.insert(0, parts[3].strip())

def update_selected():
    if selected_id is None:
        messagebox.showerror("Error", "Select a record")
        return

    update_record(
        selected_id,
        item_entry.get(),
        int(qty_entry.get()),
        loc_entry.get()
    )
    view_records()

def delete_selected():
    if selected_id is None:
        messagebox.showerror("Error", "Select a record")
        return

    delete_record(selected_id)
    view_records()
    clear_fields()

def search():
    keyword = search_entry.get()
    listbox.delete(0, tk.END)

    for row in search_records(keyword):
        listbox.insert(tk.END, f"ID:{row[0]} | {row[1]} | Qty:{row[2]} | {row[3]}")

# ---------------- NAVIGATION ---------------- #

def show_inventory():
    clear_main()
    inventory_frame.pack(fill="both", expand=True)

def show_dashboard():
    clear_main()
    dashboard_frame.pack(fill="both", expand=True)

def clear_main():
    inventory_frame.pack_forget()
    dashboard_frame.pack_forget()

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Northshore Logistics Ltd")
root.geometry("800x500")

# TOP BAR
top_frame = tk.Frame(root, bg="#2c3e50", height=50)
top_frame.pack(fill="x")

tk.Label(top_frame, text="Northshore Logistics Ltd",
         fg="white", bg="#2c3e50",
         font=("Arial", 14, "bold")).pack(side="left", padx=10)

# NAV BAR
nav_frame = tk.Frame(root, bg="#34495e")
nav_frame.pack(fill="x")

tk.Button(nav_frame, text="Dashboard", command=show_dashboard, bg="#34495e", fg="white").pack(side="left", padx=5, pady=5)
tk.Button(nav_frame, text="Inventory", command=show_inventory, bg="#34495e", fg="white").pack(side="left", padx=5)

# ---------------- DASHBOARD ---------------- #

dashboard_frame = tk.Frame(root)

tk.Label(dashboard_frame, text="Dashboard Overview",
         font=("Arial", 16, "bold")).pack(pady=20)

dashboard_text = tk.Text(dashboard_frame, height=10, width=60)
dashboard_text.pack()

def load_dashboard():
    records = get_all_records()
    dashboard_text.delete("1.0", tk.END)
    dashboard_text.insert(tk.END, f"Total Items: {len(records)}\n")

load_dashboard()

# ---------------- INVENTORY ---------------- #

inventory_frame = tk.Frame(root)

form_frame = tk.Frame(inventory_frame)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Item Name").grid(row=0, column=0)
item_entry = tk.Entry(form_frame)
item_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Quantity").grid(row=1, column=0)
qty_entry = tk.Entry(form_frame)
qty_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Location").grid(row=2, column=0)
loc_entry = tk.Entry(form_frame)
loc_entry.grid(row=2, column=1)

# BUTTONS
btn_frame = tk.Frame(inventory_frame)
btn_frame.pack()

tk.Button(btn_frame, text="Add", bg="green", fg="white", width=10, command=add_record).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Update", bg="blue", fg="white", width=10, command=update_selected).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", bg="red", fg="white", width=10, command=delete_selected).grid(row=0, column=2, padx=5)

# SEARCH
search_frame = tk.Frame(inventory_frame)
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=0)

tk.Button(search_frame, text="Search", command=search).grid(row=0, column=1, padx=5)
tk.Button(search_frame, text="View All", command=view_records).grid(row=0, column=2)

# LISTBOX
listbox = tk.Listbox(inventory_frame, width=80, height=10)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

# START DEFAULT
show_inventory()
view_records()

root.mainloop()