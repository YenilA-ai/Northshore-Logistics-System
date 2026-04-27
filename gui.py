import tkinter as tk
from tkinter import messagebox
from database import (
    insert_record,
    get_all_records,
    update_record,
    delete_record,
    search_records,
    create_table
)

create_table()

# ---------- FUNCTIONS ----------

def add_record():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    if not name or not age or not email:
        messagebox.showerror("Error", "All fields required")
        return

    try:
        age = int(age)
    except:
        messagebox.showerror("Error", "Age must be number")
        return

    insert_record(name, age, email)
    messagebox.showinfo("Success", "Record added")
    clear_fields()
    view_records()

def view_records():
    listbox.delete(0, tk.END)
    records = get_all_records()
    for r in records:
        listbox.insert(tk.END, f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")

def delete_selected():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return

    record_id = int(selected.split("|")[0])
    delete_record(record_id)
    view_records()
    clear_fields()

def update_selected():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return

    record_id = int(selected.split("|")[0])
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    if not name or not age or not email:
        messagebox.showerror("Error", "All fields required")
        return

    try:
        age = int(age)
    except:
        messagebox.showerror("Error", "Age must be number")
        return

    update_record(record_id, name, age, email)
    messagebox.showinfo("Success", "Record updated")
    view_records()
    clear_fields()

def search_record():
    keyword = search_entry.get()
    listbox.delete(0, tk.END)

    results = search_records(keyword)
    for r in results:
        listbox.insert(tk.END, f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# ---------- NEW FEATURE (AUTO-FILL) ----------

def load_selected(event):
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return

    parts = selected.split("|")

    name = parts[1].strip()
    age = parts[2].strip()
    email = parts[3].strip()

    clear_fields()

    name_entry.insert(0, name)
    age_entry.insert(0, age)
    email_entry.insert(0, email)

# ---------- UI ----------

root = tk.Tk()
root.title("Student Record Manager")
root.geometry("600x500")
root.configure(bg="#f4f6f8")

# Title
title = tk.Label(
    root,
    text="Student Record Manager",
    font=("Arial", 16, "bold"),
    bg="#f4f6f8"
)
title.grid(row=0, column=0, columnspan=4, pady=10)

# Inputs
tk.Label(root, text="Name", bg="#f4f6f8").grid(row=1, column=0, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Age", bg="#f4f6f8").grid(row=2, column=0, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

tk.Label(root, text="Email", bg="#f4f6f8").grid(row=3, column=0, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add", bg="#4CAF50", fg="white", width=12, command=add_record)\
    .grid(row=1, column=2, padx=10)

tk.Button(root, text="Update", bg="#4CAF50", fg="white", width=12, command=update_selected)\
    .grid(row=2, column=2)

tk.Button(root, text="Delete", bg="#e74c3c", fg="white", width=12, command=delete_selected)\
    .grid(row=3, column=2)

# Search
tk.Label(root, text="Search", bg="#f4f6f8").grid(row=4, column=0, pady=10)
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1)

tk.Button(root, text="Search", bg="#4CAF50", fg="white", width=12, command=search_record)\
    .grid(row=4, column=2)

tk.Button(root, text="View All", bg="#3498db", fg="white", width=12, command=view_records)\
    .grid(row=5, column=2, pady=5)

# Listbox
listbox = tk.Listbox(root, width=70, height=15)
listbox.grid(row=6, column=0, columnspan=4, pady=10)

# Bind selection event
listbox.bind("<<ListboxSelect>>", load_selected)

view_records()

root.mainloop()