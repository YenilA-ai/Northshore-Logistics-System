import tkinter as tk
from auth import login
from staff_gui import open_dashboard
from database import create_tables

create_tables()

root = tk.Tk()
root.title("Northshore Logistics Login")
root.geometry("400x300")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

def do_login():
    role = login(username.get(), password.get())

    if role:
        root.destroy()
        open_dashboard(role)
    else:
        print("Invalid login")

tk.Button(root, text="Login", command=do_login).pack(pady=10)

root.mainloop()