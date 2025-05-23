import tkinter as tk
from tkinter import messagebox
import psycopg2
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
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM FamilyVisit ORDER BY visitid")
        rows = cur.fetchall()
        listbox.delete(0, tk.END)
        for row in rows:
            listbox.insert(tk.END, row)
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_record():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO FamilyVisit (residentid, visitorname, relation, visitdate)
            VALUES (%s, %s, %s, %s)
        """, (
            entry_residentid.get(),
            entry_visitorname.get(),
            entry_relation.get(),
            entry_visitdate.get()
        ))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_record():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE FamilyVisit
            SET residentid=%s, visitorname=%s, relation=%s, visitdate=%s
            WHERE visitid=%s
        """, (
            entry_residentid.get(),
            entry_visitorname.get(),
            entry_relation.get(),
            entry_visitdate.get(),
            entry_visitid.get()
        ))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_record():
    visit_id = entry_visitid.get()
    if not visit_id:
        messagebox.showwarning("Warning", "Please select a visit to delete.")
        return
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM FamilyVisit WHERE visitid=%s", (visit_id,))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_select(event):
    try:
        index = listbox.curselection()[0]
        selected = listbox.get(index)
        entry_visitid.delete(0, tk.END)
        entry_visitid.insert(tk.END, selected[0])
        entry_residentid.delete(0, tk.END)
        entry_residentid.insert(tk.END, selected[1])
        entry_visitorname.delete(0, tk.END)
        entry_visitorname.insert(tk.END, selected[2])
        entry_visitdate.delete(0, tk.END)
        entry_visitdate.insert(tk.END, selected[3])
        entry_relation.delete(0, tk.END)
        entry_relation.insert(tk.END, selected[4])
    except Exception as e:
        print("Selection error:", e)

def clear_fields():
    entry_visitid.delete(0, tk.END)
    entry_residentid.delete(0, tk.END)
    entry_visitorname.delete(0, tk.END)
    entry_relation.delete(0, tk.END)
    entry_visitdate.delete(0, tk.END)

def back_to_main():
    root.destroy()

root = tk.Tk()
root.title("Family Visit Management")
root.geometry("550x500")

tk.Label(root, text="Visit ID").grid(row=0, column=0)
tk.Label(root, text="Resident ID").grid(row=1, column=0)
tk.Label(root, text="Visitor Name").grid(row=2, column=0)
tk.Label(root, text="Relation").grid(row=3, column=0)
tk.Label(root, text="Visit Date (YYYY-MM-DD)").grid(row=4, column=0)

entry_visitid = tk.Entry(root)
entry_residentid = tk.Entry(root)
entry_visitorname = tk.Entry(root)
entry_relation = tk.Entry(root)
entry_visitdate = tk.Entry(root)

entry_visitid.grid(row=0, column=1)
entry_residentid.grid(row=1, column=1)
entry_visitorname.grid(row=2, column=1)
entry_relation.grid(row=3, column=1)
entry_visitdate.grid(row=4, column=1)

tk.Button(root, text="Insert", command=insert_record).grid(row=5, column=0, pady=5)
tk.Button(root, text="Update", command=update_record).grid(row=5, column=1)
tk.Button(root, text="Delete", command=delete_record).grid(row=5, column=2)
tk.Button(root, text="Back", command=back_to_main).grid(row=6, column=1, pady=5)

listbox = tk.Listbox(root, width=80)
listbox.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
listbox.bind('<<ListboxSelect>>', on_select)

refresh_data()
root.mainloop()