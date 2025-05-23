import tkinter as tk
from tkinter import ttk, messagebox
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

def run_query_2():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                medicalstatus,
                gender,
                ROUND(AVG(EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM dateofbirth))) AS average_age,
                COUNT(*) AS total_residents
            FROM 
                resident
            GROUP BY 
                medicalstatus, gender
            ORDER BY 
                average_age DESC;
        """)
        rows = cur.fetchall()
        display_result(rows, ['Medical Status', 'Gender', 'Average Age', 'Total'])
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Query Error", str(e))

def run_query_4():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                r.firstname || ' ' || r.lastname AS full_name,
                r.gender,
                EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM r.dateofbirth) AS age,
                (CURRENT_DATE - r.admissiondate)::INT AS days_in_facility,
                d.name AS department_name
            FROM 
                resident r
            JOIN 
                room rm ON r.roomid = rm.roomid
            JOIN 
                department d ON rm.departmentid = d.departmentid
            ORDER BY 
                days_in_facility DESC;
        """)
        rows = cur.fetchall()
        display_result(rows, ['Full Name', 'Gender', 'Age', 'Days in Facility', 'Department'])
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Query Error", str(e))

def display_result(rows, headers):
    for widget in result_frame.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(result_frame, columns=headers, show='headings')
    for header in headers:
        tree.heading(header, text=header)
        tree.column(header, width=150)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)

def back_to_main():
    root.destroy()

root = tk.Tk()
root.title("Query Viewer")
root.geometry("900x500")

tk.Label(root, text="Select a query to run:").pack(pady=10)

tk.Button(root, text="Average Age by Status & Gender", command=run_query_2, width=40).pack(pady=5)
tk.Button(root, text="Resident Details & Stay Duration", command=run_query_4, width=40).pack(pady=5)
tk.Button(root, text="Back to Main Menu", command=back_to_main, width=20).pack(pady=10)

result_frame = tk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()