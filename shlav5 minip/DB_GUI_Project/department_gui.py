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
        cur.execute("SELECT * FROM Department ORDER BY departmentid")
        rows = cur.fetchall()
        listbox.delete(0, tk.END)
        for row in rows:
            display = f"{row[0]} {{{row[1]}}} {{{row[2]}}} {row[3]}"
            listbox.insert(tk.END, display)
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_record():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Department (name, manager, phone)
            VALUES (%s, %s, %s)
        """, (
            entry_name.get(),
            entry_manager.get(),
            entry_phone.get()
        ))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_record():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE Department
            SET name=%s, manager=%s, phone=%s
            WHERE departmentid=%s
        """, (
            entry_name.get(),
            entry_manager.get(),
            entry_phone.get(),
            entry_departmentid.get()
        ))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_record():
    try:
        dept_id = entry_departmentid.get().strip()
        if not dept_id:
            messagebox.showwarning("Warning", "Please select a department to delete.")
            return
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM Department WHERE departmentid = %s", (dept_id,))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_select(event):
    try:
        selected = listbox.get(listbox.curselection())
        parts = selected.split(" ", 1)
        dept_id = parts[0]
        rest = parts[1].split("{")
        name = rest[1].split("}")[0]
        manager = rest[2].split("}")[0]
        phone = selected.split("}")[-1].strip()

        entry_departmentid.delete(0, tk.END)
        entry_departmentid.insert(0, dept_id)
        entry_name.delete(0, tk.END)
        entry_name.insert(0, name)
        entry_manager.delete(0, tk.END)
        entry_manager.insert(0, manager)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, phone)
    except Exception as e:
        print("Error selecting item:", e)

def clear_fields():
    entry_departmentid.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_manager.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def back_to_main():
    root.destroy()

root = tk.Tk()
root.title("Department Management")
root.geometry("550x500")

tk.Label(root, text="Department ID").grid(row=0, column=0)
tk.Label(root, text="Name").grid(row=1, column=0)
tk.Label(root, text="Manager").grid(row=2, column=0)
tk.Label(root, text="Phone").grid(row=3, column=0)

entry_departmentid = tk.Entry(root)
entry_name = tk.Entry(root)
entry_manager = tk.Entry(root)
entry_phone = tk.Entry(root)

entry_departmentid.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_manager.grid(row=2, column=1)
entry_phone.grid(row=3, column=1)

tk.Button(root, text="Insert", command=insert_record).grid(row=4, column=0, pady=5)
tk.Button(root, text="Update", command=update_record).grid(row=4, column=1)
tk.Button(root, text="Delete", command=delete_record).grid(row=4, column=2)
tk.Button(root, text="Back", command=back_to_main).grid(row=5, column=1, pady=5)

listbox = tk.Listbox(root, width=80)
listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
listbox.bind('<<ListboxSelect>>', on_select)

refresh_data()
root.mainloop()