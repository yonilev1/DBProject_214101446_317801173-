import tkinter as tk
from tkinter import messagebox
import psycopg2
import db_config
from datetime import datetime

def connect():
    return psycopg2.connect(
        dbname=db_config.DB_NAME,
        user=db_config.DB_USER,
        password=db_config.DB_PASSWORD,
        host=db_config.DB_HOST,
        port=db_config.DB_PORT
    )

def run_fn_count_medications():
    try:
        resident_id = int(entry_resident_id.get())
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT fn_count_medications(%s)", (resident_id,))
        result = cur.fetchone()[0]
        messagebox.showinfo("Result", f"Number of medications: {result}")
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_fn_total_treatments():
    try:
        treatment_type = entry_treatment_type.get()
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT fn_total_treatments_by_type(%s)", (treatment_type,))
        result = cur.fetchone()[0]
        messagebox.showinfo("Result", f"Total treatments: {result}")
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_sp_update_status():
    try:
        resident_id = int(entry_resident_id_update.get())
        new_status = entry_new_status.get()
        conn = connect()
        cur = conn.cursor()
        cur.execute("CALL sp_update_medical_status(%s, %s)", (resident_id, new_status))
        conn.commit()
        messagebox.showinfo("Success", "Status updated.")
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_sp_add_caregiver():
    try:
        fname = entry_fname.get()
        lname = entry_lname.get()
        dept_id = int(entry_deptid.get())
        hiredate = datetime.strptime(entry_hiredate.get(), "%Y-%m-%d").date()
        phone = entry_phone.get()

        conn = connect()
        cur = conn.cursor()
        cur.execute("CALL sp_add_caregiver(%s, %s, %s, %s, %s)", (fname, lname, dept_id, hiredate, phone))
        conn.commit()
        messagebox.showinfo("Success", "Caregiver added.")
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def back():
    root.destroy()

root = tk.Tk()
root.title("Functions & Procedures")
root.geometry("600x500")

# Function 1
tk.Label(root, text="Count Medications for Resident ID:").pack()
entry_resident_id = tk.Entry(root)
entry_resident_id.pack()
tk.Button(root, text="Run fn_count_medications", command=run_fn_count_medications).pack(pady=5)

# Function 2
tk.Label(root, text="Total Treatments of Type:").pack()
entry_treatment_type = tk.Entry(root)
entry_treatment_type.pack()
tk.Button(root, text="Run fn_total_treatments_by_type", command=run_fn_total_treatments).pack(pady=5)

# Procedure 1
tk.Label(root, text="Update Medical Status - Resident ID:").pack()
entry_resident_id_update = tk.Entry(root)
entry_resident_id_update.pack()
tk.Label(root, text="New Status:").pack()
entry_new_status = tk.Entry(root)
entry_new_status.pack()
tk.Button(root, text="Run sp_update_medical_status", command=run_sp_update_status).pack(pady=5)

# Procedure 2
tk.Label(root, text="Add Caregiver - First Name:").pack()
entry_fname = tk.Entry(root)
entry_fname.pack()
tk.Label(root, text="Last Name:").pack()
entry_lname = tk.Entry(root)
entry_lname.pack()
tk.Label(root, text="Department ID:").pack()
entry_deptid = tk.Entry(root)
entry_deptid.pack()
tk.Label(root, text="Hire Date (YYYY-MM-DD):").pack()
entry_hiredate = tk.Entry(root)
entry_hiredate.pack()
tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()
tk.Button(root, text="Run sp_add_caregiver", command=run_sp_add_caregiver).pack(pady=5)

# Back button
tk.Button(root, text="Back to Menu", command=back).pack(pady=10)

root.mainloop()