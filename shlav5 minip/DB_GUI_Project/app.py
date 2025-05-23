import tkinter as tk
import subprocess
import sys

def open_residents():
    subprocess.Popen([sys.executable, "residents_gui.py"])

def open_medical_treatments():
    subprocess.Popen([sys.executable, "medicaltreatment_gui.py"])

def open_caregivers():
    subprocess.Popen([sys.executable, "caregivers_gui.py"])

def open_medications():
    subprocess.Popen([sys.executable, "medications_gui.py"])

def open_resident_medications():
    subprocess.Popen([sys.executable, "residentmedications_gui.py"])

def open_family_visits():
    subprocess.Popen([sys.executable, "familyvisit_gui.py"])

def open_departments():
    subprocess.Popen([sys.executable, "department_gui.py"])

def open_rooms():
    subprocess.Popen([sys.executable, "room_gui.py"])

def open_func_proce():
    subprocess.Popen([sys.executable, "functions_procedures_gui.py"])

def open_queries():
    subprocess.Popen([sys.executable, "queries_gui.py"])

root = tk.Tk()
root.title("Main Menu")
root.geometry("400x400")

tk.Label(root, text="Welcome to the Nursing Home System", font=("Helvetica", 16)).pack(pady=20)

tk.Button(root, text="Residents", width=25, command=open_residents).pack(pady=5)
tk.Button(root, text="Medical Treatments", width=25, command=open_medical_treatments).pack(pady=5)
tk.Button(root, text="Caregivers", width=25, command=open_caregivers).pack(pady=5)
tk.Button(root, text="Medications", width=25, command=open_medications).pack(pady=5)
tk.Button(root, text="Resident Medications", width=25, command=open_resident_medications).pack(pady=5)
tk.Button(root, text="Family Visits", width=30, command=open_family_visits).pack(pady=5)
tk.Button(root, text="Departments", width=30, command=open_departments).pack(pady=5)
tk.Button(root, text="Rooms", width=30, command=open_rooms).pack(pady=5)
tk.Button(root, text="functions & procedures", width=30, command=open_func_proce).pack(pady=5)
tk.Button(root, text="queries", width=30, command=open_queries).pack(pady=5)



# אפשר להוסיף כאן עוד כפתורים למסכים הבאים...

root.mainloop()