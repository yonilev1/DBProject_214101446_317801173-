import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
import db_config
import subprocess
import sys


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
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM medicaltreatment ORDER BY treatmentid")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    cur.close()
    conn.close()


def add_treatment():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO medicaltreatment (
                residentid, caregiverid, treatmentdate, treatmenttype,
                followupdate, notes, treatmenttime, purpose, status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            e_residentid.get(), e_caregiverid.get(), e_date.get(), e_type.get(),
            e_followup.get(), e_notes.get(), e_time.get(), e_purpose.get(), e_status.get()
        ))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        messagebox.showinfo("Success", "Treatment added.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_treatment():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select", "Please select a treatment to update.")
        return
    item = tree.item(selected[0])
    treatmentid = item["values"][0]

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE medicaltreatment SET
                residentid=%s,
                caregiverid=%s,
                treatmentdate=%s,
                treatmenttype=%s,
                followupdate=%s,
                notes=%s,
                treatmenttime=%s,
                purpose=%s,
                status=%s
            WHERE treatmentid=%s
        """, (
            e_residentid.get(), e_caregiverid.get(), e_date.get(), e_type.get(),
            e_followup.get(), e_notes.get(), e_time.get(), e_purpose.get(), e_status.get(),
            treatmentid
        ))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        messagebox.showinfo("Updated", "Treatment updated.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_treatment():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select", "Please select a treatment to delete.")
        return
    item = tree.item(selected[0])
    treatmentid = item["values"][0]
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM medicaltreatment WHERE treatmentid = %s", (treatmentid,))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        messagebox.showinfo("Deleted", "Treatment deleted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def on_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])
        values = item["values"]
        e_residentid.delete(0, tk.END)
        e_residentid.insert(0, values[1])
        e_caregiverid.delete(0, tk.END)
        e_caregiverid.insert(0, values[2])
        e_date.delete(0, tk.END)
        e_date.insert(0, values[3])
        e_type.delete(0, tk.END)
        e_type.insert(0, values[4])
        e_followup.delete(0, tk.END)
        e_followup.insert(0, values[5])
        e_notes.delete(0, tk.END)
        e_notes.insert(0, values[6])
        e_time.delete(0, tk.END)
        e_time.insert(0, values[7])
        e_purpose.delete(0, tk.END)
        e_purpose.insert(0, values[8])
        e_status.delete(0, tk.END)
        e_status.insert(0, values[9])


def go_back_to_main_menu():
    root.destroy()
    subprocess.Popen([sys.executable, "app.py"])


# GUI layout
root = tk.Tk()
root.title("Medical Treatments Management")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Resident ID").grid(row=0, column=0)
tk.Label(frame, text="Caregiver ID").grid(row=0, column=2)
tk.Label(frame, text="Treatment Date").grid(row=1, column=0)
tk.Label(frame, text="Treatment Type").grid(row=1, column=2)
tk.Label(frame, text="Follow Up").grid(row=2, column=0)
tk.Label(frame, text="Notes").grid(row=2, column=2)
tk.Label(frame, text="Treatment Time").grid(row=3, column=0)
tk.Label(frame, text="Purpose").grid(row=3, column=2)
tk.Label(frame, text="Status").grid(row=4, column=0)

e_residentid = tk.Entry(frame)
e_caregiverid = tk.Entry(frame)
e_date = tk.Entry(frame)
e_type = tk.Entry(frame)
e_followup = tk.Entry(frame)
e_notes = tk.Entry(frame)
e_time = tk.Entry(frame)
e_purpose = tk.Entry(frame)
e_status = tk.Entry(frame)

e_residentid.grid(row=0, column=1)
e_caregiverid.grid(row=0, column=3)
e_date.grid(row=1, column=1)
e_type.grid(row=1, column=3)
e_followup.grid(row=2, column=1)
e_notes.grid(row=2, column=3)
e_time.grid(row=3, column=1)
e_purpose.grid(row=3, column=3)
e_status.grid(row=4, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Add", width=12, command=add_treatment).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Update", width=12, command=update_treatment).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_treatment).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Back to Menu", width=14, command=go_back_to_main_menu).pack(side=tk.LEFT, padx=5)

tree = ttk.Treeview(root, columns=("id", "resident", "caregiver", "date", "type", "followup", "notes", "time", "purpose", "status"), show="headings")
tree.pack(padx=10, pady=10)

cols = ["Treatment ID", "Resident ID", "Caregiver ID", "Date", "Type", "FollowUp", "Notes", "Time", "Purpose", "Status"]
for i, col in enumerate(cols):
    tree.heading(i, text=col)
    tree.column(i, width=100)

tree.bind("<<TreeviewSelect>>", on_select)

refresh_data()
root.mainloop()