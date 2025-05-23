import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import sys
import subprocess
import db_config

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
        cur.execute("SELECT * FROM ResidentMedications ORDER BY residentmedicationid;")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_entry():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO ResidentMedications (residentid, medicationid, dosage, frequency, startdate, enddate, prescribedby)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            residentid_var.get(),
            medicationid_var.get(),
            dosage_var.get(),
            frequency_var.get(),
            startdate_var.get(),
            enddate_var.get(),
            prescribedby_var.get()
        ))
        conn.commit()
        conn.close()
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_entry():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select", "Please select a row to update.")
        return
    values = tree.item(selected, 'values')
    record_id = values[0]
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE ResidentMedications
            SET residentid=%s, medicationid=%s, dosage=%s, frequency=%s,
                startdate=%s, enddate=%s, prescribedby=%s
            WHERE residentmedicationid=%s
        """, (
            residentid_var.get(),
            medicationid_var.get(),
            dosage_var.get(),
            frequency_var.get(),
            startdate_var.get(),
            enddate_var.get(),
            prescribedby_var.get(),
            record_id
        ))
        conn.commit()
        conn.close()
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_entry():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select", "Please select a row to delete.")
        return
    values = tree.item(selected, 'values')
    record_id = values[0]
    confirm = messagebox.askyesno("Confirm", f"Delete record ID {record_id}?")
    if confirm:
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("DELETE FROM ResidentMedications WHERE residentmedicationid=%s", (record_id,))
            conn.commit()
            conn.close()
            refresh_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def select_row(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        residentid_var.set(values[1])
        medicationid_var.set(values[2])
        dosage_var.set(values[3])
        frequency_var.set(values[4])
        startdate_var.set(values[5])
        enddate_var.set(values[6])
        prescribedby_var.set(values[7])

def go_back_to_main_menu():
    root.destroy()
    subprocess.Popen([sys.executable, "app.py"])

# GUI
root = tk.Tk()
root.title("Resident Medications Management")
root.geometry("950x600")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

residentid_var = tk.StringVar()
medicationid_var = tk.StringVar()
dosage_var = tk.StringVar()
frequency_var = tk.StringVar()
startdate_var = tk.StringVar()
enddate_var = tk.StringVar()
prescribedby_var = tk.StringVar()

fields = [
    ("Resident ID", residentid_var),
    ("Medication ID", medicationid_var),
    ("Dosage", dosage_var),
    ("Frequency", frequency_var),
    ("Start Date", startdate_var),
    ("End Date", enddate_var),
    ("Prescribed By", prescribedby_var),
]

for i, (label, var) in enumerate(fields):
    tk.Label(input_frame, text=label).grid(row=0, column=i)
    tk.Entry(input_frame, textvariable=var, width=14).grid(row=1, column=i, padx=4)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=14, command=add_entry).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Update", width=14, command=update_entry).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete", width=14, command=delete_entry).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Back to Menu", width=14, command=go_back_to_main_menu).pack(side=tk.LEFT, padx=5)

tree = ttk.Treeview(root, columns=("ID", "ResidentID", "MedicationID", "Dosage", "Frequency", "StartDate", "EndDate", "PrescribedBy"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=110)
tree.pack(pady=20, fill=tk.X)
tree.bind("<<TreeviewSelect>>", select_row)

refresh_data()
root.mainloop()