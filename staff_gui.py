import tkinter as tk

def open_dashboard(role):
    root = tk.Tk()
    root.title("Northshore Logistics Ltd")
    root.geometry("900x550")

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    def clear():
        for w in frame.winfo_children():
            w.destroy()

    def dashboard():
        clear()
        tk.Label(frame, text=f"{role} Dashboard", font=("Arial", 18)).pack()

    def register_user():
        clear()
        tk.Label(frame, text="Register User").pack()

    def shipments():
        clear()
        tk.Label(frame, text="Shipments Module").pack()

    def inventory():
        clear()
        tk.Label(frame, text="Inventory Module").pack()

    def vehicles():
        clear()
        tk.Label(frame, text="Vehicles Module").pack()

    def drivers():
        clear()
        tk.Label(frame, text="Drivers Module").pack()

    def reports():
        clear()
        tk.Label(frame, text="Reports").pack()

    def logs():
        clear()
        tk.Label(frame, text="Logs").pack()

    # NAVBAR
    nav = tk.Frame(root, bg="#2c3e50")
    nav.pack(fill="x")

    tk.Button(nav, text="Dashboard", command=dashboard).pack(side="left")

    if role == "admin":
        tk.Button(nav, text="Register", command=register_user).pack(side="left")
        tk.Button(nav, text="Reports", command=reports).pack(side="left")
        tk.Button(nav, text="Logs", command=logs).pack(side="left")

    tk.Button(nav, text="Inventory", command=inventory).pack(side="left")
    tk.Button(nav, text="Vehicles", command=vehicles).pack(side="left")
    tk.Button(nav, text="Shipments", command=shipments).pack(side="left")
    tk.Button(nav, text="Drivers", command=drivers).pack(side="left")

    dashboard()

    root.mainloop()