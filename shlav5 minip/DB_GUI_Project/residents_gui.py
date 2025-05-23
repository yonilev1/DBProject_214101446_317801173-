# residents_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import db_config

# connect to database
def connect():
    return psycopg2.connect(
        dbname=db_config.DB_NAME,
        user=db_config.DB_USER,
        password=db_config.DB_PASSWORD,
        host=db_config.DB_HOST,
        port=db_config.DB_PORT
    )

# refresh the table view
def refresh_data():
    for row in tree.get_children():
        tree.delete(row)
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT residentid, firstname, lastname, gender, medicalstatus FROM resident ORDER BY residentid")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    cur.close()
    conn.close()

# add resident
def add_resident():
    fname = entry_fname.get()
    lname = entry_lname.get()
    gender = entry_gender.get()
    status = entry_status.get()
    if not (fname and lname and gender and status):
        messagebox.showwarning("Missing info", "Please fill all fields.")
        return
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO resident (firstname, lastname, gender, medicalstatus)
            VALUES (%s, %s, %s, %s)
        """, (fname, lname, gender, status))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        entry_fname.delete(0, tk.END)
        entry_lname.delete(0, tk.END)
        entry_gender.delete(0, tk.END)
        entry_status.delete(0, tk.END)
        messagebox.showinfo("Success", "Resident added.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# delete resident
def delete_resident():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a resident to delete.")
        return

    resident_id = tree.item(selected[0])['values'][0]

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete resident ID {resident_id} and all related records?")
    if not confirm:
        return

    try:
        conn = connect()
        cur = conn.cursor()
        # מחיקת רשומות תלויות
        cur.execute("DELETE FROM residentmedications WHERE residentid = %s", (resident_id,))
        cur.execute("DELETE FROM medicaltreatment WHERE residentid = %s", (resident_id,))
        cur.execute("DELETE FROM familyvisit WHERE residentid = %s", (resident_id,))
        # מחיקת הדייר עצמו
        cur.execute("DELETE FROM resident WHERE residentid = %s", (resident_id,))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        messagebox.showinfo("Success", "Resident deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# update resident
def update_resident():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select row", "Please select a resident to update.")
        return
    item = tree.item(selected[0])
    resident_id = item["values"][0]
    fname = entry_fname.get()
    lname = entry_lname.get()
    gender = entry_gender.get()
    status = entry_status.get()
    if not (fname and lname and gender and status):
        messagebox.showwarning("Missing info", "Please fill all fields.")
        return
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE resident
            SET firstname = %s, lastname = %s, gender = %s, medicalstatus = %s
            WHERE residentid = %s
        """, (fname, lname, gender, status, resident_id))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        messagebox.showinfo("Updated", "Resident updated.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Residents Management")
root.geometry("700x500")

tk.Label(root, text="First Name").grid(row=0, column=0)
entry_fname = tk.Entry(root)
entry_fname.grid(row=0, column=1)

tk.Label(root, text="Last Name").grid(row=1, column=0)
entry_lname = tk.Entry(root)
entry_lname.grid(row=1, column=1)

tk.Label(root, text="Gender").grid(row=2, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=2, column=1)

tk.Label(root, text="Medical Status").grid(row=3, column=0)
entry_status = tk.Entry(root)
entry_status.grid(row=3, column=1)

tk.Button(root, text="Add", command=add_resident).grid(row=4, column=0, pady=10)
tk.Button(root, text="Update", command=update_resident).grid(row=4, column=1)
tk.Button(root, text="Delete", command=delete_resident).grid(row=4, column=2)

tree = ttk.Treeview(root, columns=("ID", "First", "Last", "Gender", "Status"), show="headings")
tree.heading("ID", text="ID")
tree.heading("First", text="First Name")
tree.heading("Last", text="Last Name")
tree.heading("Gender", text="Gender")
tree.heading("Status", text="Medical Status")
tree.grid(row=5, column=0, columnspan=5, padx=10, pady=20, sticky="nsew")

refresh_data()

root.mainloop()