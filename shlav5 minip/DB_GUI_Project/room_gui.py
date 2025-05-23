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
        cur.execute("SELECT * FROM Room ORDER BY roomid")
        rows = cur.fetchall()
        listbox.delete(0, tk.END)
        for row in rows:
            listbox.insert(tk.END, row)
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_fields():
    entry_roomid.delete(0, tk.END)
    entry_floor.delete(0, tk.END)
    entry_roomnumber.delete(0, tk.END)
    entry_capacity.delete(0, tk.END)
    entry_roomtype.delete(0, tk.END)
    entry_departmentid.delete(0, tk.END)

def insert_record():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Room (floor, roomnumber, capacity, roomtype, departmentid)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            entry_floor.get(),
            entry_roomnumber.get(),
            entry_capacity.get(),
            entry_roomtype.get(),
            entry_departmentid.get()
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
        room_id = entry_roomid.get().strip()
        if not room_id:
            messagebox.showwarning("Warning", "Please select a room to update.")
            return
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE Room
            SET floor=%s, roomnumber=%s, capacity=%s, roomtype=%s, departmentid=%s
            WHERE roomid=%s
        """, (
            entry_floor.get(),
            entry_roomnumber.get(),
            entry_capacity.get(),
            entry_roomtype.get(),
            entry_departmentid.get(),
            room_id
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
        room_id = entry_roomid.get().strip()
        if not room_id:
            messagebox.showwarning("Warning", "Please select a room to delete.")
            return
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM Room WHERE roomid = %s", (room_id,))
        conn.commit()
        cur.close()
        conn.close()
        refresh_data()
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_select(event):
    selected = listbox.curselection()
    if selected:
        values = listbox.get(selected[0])
        entry_roomid.delete(0, tk.END)
        entry_roomid.insert(0, values[0])
        entry_floor.delete(0, tk.END)
        entry_floor.insert(0, values[1])
        entry_roomnumber.delete(0, tk.END)
        entry_roomnumber.insert(0, values[2])
        entry_capacity.delete(0, tk.END)
        entry_capacity.insert(0, values[3])
        entry_roomtype.delete(0, tk.END)
        entry_roomtype.insert(0, values[4])
        entry_departmentid.delete(0, tk.END)
        entry_departmentid.insert(0, values[5])

def back_to_main():
    root.destroy()

root = tk.Tk()
root.title("Room Management")
root.geometry("600x500")

tk.Label(root, text="Room ID").grid(row=0, column=0)
tk.Label(root, text="Floor").grid(row=1, column=0)
tk.Label(root, text="Room Number").grid(row=2, column=0)
tk.Label(root, text="Capacity").grid(row=3, column=0)
tk.Label(root, text="Room Type").grid(row=4, column=0)
tk.Label(root, text="Department ID").grid(row=5, column=0)

entry_roomid = tk.Entry(root)
entry_floor = tk.Entry(root)
entry_roomnumber = tk.Entry(root)
entry_capacity = tk.Entry(root)
entry_roomtype = tk.Entry(root)
entry_departmentid = tk.Entry(root)

entry_roomid.grid(row=0, column=1)
entry_floor.grid(row=1, column=1)
entry_roomnumber.grid(row=2, column=1)
entry_capacity.grid(row=3, column=1)
entry_roomtype.grid(row=4, column=1)
entry_departmentid.grid(row=5, column=1)

tk.Button(root, text="Insert", command=insert_record).grid(row=6, column=0, pady=5)
tk.Button(root, text="Update", command=update_record).grid(row=6, column=1)
tk.Button(root, text="Delete", command=delete_record).grid(row=6, column=2)
tk.Button(root, text="Back", command=back_to_main).grid(row=7, column=1, pady=5)

listbox = tk.Listbox(root, width=80)
listbox.grid(row=8, column=0, columnspan=3, padx=10, pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

refresh_data()
root.mainloop()