import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
import sys
import subprocess
import db_config  # קובץ החיבור שלך

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
        cur.execute("SELECT * FROM Medications ORDER BY medicationid;")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_medication():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Medications (name, description, manufacturer)
            VALUES (%s, %s, %s)
        """, (name_var.get(), description_var.get(), manufacturer_var.get()))
        conn.commit()
        conn.close()
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_medication():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select", "Please select a row first.")
        return
    values = tree.item(selected, 'values')
    medicationid = values[0]
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE Medications SET name=%s, description=%s, manufacturer=%s
            WHERE medicationid=%s
        """, (name_var.get(), description_var.get(), manufacturer_var.get(), medicationid))
        conn.commit()
        conn.close()
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_medication():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a medication to delete.")
        return

    medication_id = tree.item(selected[0])['values'][0]

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete medication ID {medication_id} and related records?")
    if not confirm:
        return

    try:
        conn = connect()
        cur = conn.cursor()
        # מחיקת התלויות קודם
        cur.execute("DELETE FROM residentmedications WHERE medicationid = %s", (medication_id,))
        # ואז מחיקת התרופה
        cur.execute("DELETE FROM medications WHERE medicationid = %s", (medication_id,))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        messagebox.showinfo("Success", "Medication deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_row(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        name_var.set(values[1])
        description_var.set(values[2])
        manufacturer_var.set(values[3])

def go_back_to_main_menu():
    root.destroy()
    subprocess.Popen([sys.executable, "app.py"])

# GUI
root = tk.Tk()
root.title("Medications Management")
root.geometry("850x600")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

name_var = tk.StringVar()
description_var = tk.StringVar()
manufacturer_var = tk.StringVar()

fields = [
    ("Name", name_var),
    ("Description", description_var),
    ("Manufacturer", manufacturer_var)
]

for i, (label, var) in enumerate(fields):
    tk.Label(input_frame, text=label).grid(row=0, column=i)
    tk.Entry(input_frame, textvariable=var).grid(row=1, column=i, padx=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=14, command=add_medication).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Update", width=14, command=update_medication).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete", width=14, command=delete_medication).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Back to Menu", width=14, command=go_back_to_main_menu).pack(side=tk.LEFT, padx=5)

tree = ttk.Treeview(root, columns=("ID", "Name", "Description", "Manufacturer"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=180)
tree.pack(pady=20, fill=tk.X)
tree.bind("<<TreeviewSelect>>", select_row)

refresh_data()
root.mainloop()