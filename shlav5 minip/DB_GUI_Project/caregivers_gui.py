import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
import sys
import subprocess
import db_config  # משתמש בקובץ config.py שלך

def connect():
    return psycopg2.connect(
        dbname=db_config.DB_NAME,
        user=db_config.DB_USER,
        password=db_config.DB_PASSWORD,
        host=db_config.DB_HOST,
        port=db_config.DB_PORT
    )

def refresh_data():
    for row in tree.get_children():
        tree.delete(row)
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Caregiver ORDER BY caregiverid;")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_caregiver():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Caregiver (firstname, lastname, departmentid, hiredate, phone)
            VALUES (%s, %s, %s, %s, %s)
        """, (firstname_var.get(), lastname_var.get(), deptid_var.get(), hiredate_var.get(), phone_var.get()))
        conn.commit()
        conn.close()
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_caregiver():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select", "Please select a row first.")
        return
    values = tree.item(selected, 'values')
    caregiverid = values[0]
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE Caregiver SET firstname=%s, lastname=%s, departmentid=%s, hiredate=%s, phone=%s
            WHERE caregiverid=%s
        """, (firstname_var.get(), lastname_var.get(), deptid_var.get(), hiredate_var.get(), phone_var.get(), caregiverid))
        conn.commit()
        conn.close()
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_caregiver():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select", "Please select a row first.")
        return
    values = tree.item(selected, 'values')
    caregiverid = values[0]
    confirm = messagebox.askyesno("Confirm", f"Delete caregiver ID {caregiverid}?")
    if confirm:
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("DELETE FROM Caregiver WHERE caregiverid=%s", (caregiverid,))
            conn.commit()
            conn.close()
            refresh_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def select_row(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        firstname_var.set(values[1])
        lastname_var.set(values[2])
        deptid_var.set(values[3])
        hiredate_var.set(values[4])
        phone_var.set(values[5])

def go_back_to_main_menu():
    root.destroy()
    subprocess.Popen([sys.executable, "app.py"])

# GUI setup
root = tk.Tk()
root.title("Caregivers Management")
root.geometry("900x600")

# Input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

firstname_var = tk.StringVar()
lastname_var = tk.StringVar()
deptid_var = tk.StringVar()
hiredate_var = tk.StringVar()
phone_var = tk.StringVar()

fields = [
    ("First Name", firstname_var),
    ("Last Name", lastname_var),
    ("Department ID", deptid_var),
    ("Hire Date (YYYY-MM-DD)", hiredate_var),
    ("Phone", phone_var)
]

for i, (label, var) in enumerate(fields):
    tk.Label(input_frame, text=label).grid(row=0, column=i)
    tk.Entry(input_frame, textvariable=var).grid(row=1, column=i, padx=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=14, command=add_caregiver).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Update", width=14, command=update_caregiver).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete", width=14, command=delete_caregiver).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Back to Menu", width=14, command=go_back_to_main_menu).pack(side=tk.LEFT, padx=5)

# Table
tree = ttk.Treeview(root, columns=("ID", "First Name", "Last Name", "DeptID", "Hire Date", "Phone"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=140)
tree.pack(pady=20, fill=tk.X)
tree.bind("<<TreeviewSelect>>", select_row)

refresh_data()
root.mainloop()