import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import webbrowser
import ttkbootstrap as tb

EXCEL_FILE = "job_applications.xlsx"
COLUMNS = ["Job Title", "Company Name", "Location", "Job Link", "Applied Date", "Status", "Comments"]
STATUS_OPTIONS = ["Initial Call", "HR Call", "Tech Interview", "Manager Interview", "Waiting", "Custom"]

def load_excel():
    if os.path.exists(EXCEL_FILE):
        return pd.read_excel(EXCEL_FILE)
    else:
        return pd.DataFrame(columns=COLUMNS)

def save_excel(df):
    df.to_excel(EXCEL_FILE, index=False)

def open_excel():
    if os.path.exists(EXCEL_FILE):
        os.system(f"start {EXCEL_FILE}")
    else:
        messagebox.showerror("Error", "Excel file not found!")

def add_comment():
    selected_item = job_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a job to add a comment")
        return
    
    df = load_excel()
    index = int(job_table.item(selected_item)['text'])
    comment = simpledialog.askstring("Add Comment", "Enter your comment:")
    if comment:
        df.at[index, "Comments"] = comment
        save_excel(df)
        update_table(df)
        messagebox.showinfo("Success", "Comment added successfully!")

def add_job():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a job URL")
        return
    
    df = load_excel()
    if url in df["Job Link"].values:
        messagebox.showwarning("Warning", "This job is already in the list!")
        return
    
    title = simpledialog.askstring("Input", "Enter Job Title:")
    company = simpledialog.askstring("Input", "Enter Company Name:")
    location = simpledialog.askstring("Input", "Enter Job Location:")
    
    new_entry = pd.DataFrame([[title, company, location, url, "", "", ""]], columns=COLUMNS)
    df = pd.concat([df, new_entry], ignore_index=True)
    save_excel(df)
    update_table(df)
    messagebox.showinfo("Success", "Job added successfully!")

def update_applied_date():
    selected_item = job_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a job to mark as applied")
        return
    
    df = load_excel()
    index = int(job_table.item(selected_item)['text'])
    df.at[index, "Applied Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.at[index, "Status"] = "Applied"
    save_excel(df)
    update_table(df)
    messagebox.showinfo("Success", "Job marked as applied!")

def update_status():
    selected_item = job_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a job to update status")
        return
    
    df = load_excel()
    index = int(job_table.item(selected_item)['text'])
    
    status_window = tk.Toplevel(root)
    status_window.title("Update Status")
    status_window.geometry("300x300")
    
    selected_status = tk.StringVar(value=STATUS_OPTIONS[0])
    
    def confirm_status():
        new_status = selected_status.get()
        if new_status == "Custom":
            new_status = simpledialog.askstring("Custom Status", "Enter your custom status:")
        df.at[index, "Status"] = new_status
        save_excel(df)
        update_table(df)
        status_window.destroy()
        messagebox.showinfo("Success", f"Status updated to {new_status}!")
    
    for option in STATUS_OPTIONS:
        ttk.Radiobutton(status_window, text=option, variable=selected_status, value=option).pack(anchor="w")
    
    ttk.Button(status_window, text="Confirm", command=confirm_status).pack(pady=10)

def delete_entry():
    selected_item = job_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a job to delete")
        return
    
    df = load_excel()
    index = int(job_table.item(selected_item)['text'])
    df.drop(index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    save_excel(df)
    update_table(df)
    messagebox.showinfo("Success", "Job entry deleted!")

def update_table(df):
    job_table.delete(*job_table.get_children())
    for i, row in df.iterrows():
        job_table.insert("", "end", text=i, values=row.tolist())

def load_existing_data():
    df = load_excel()
    update_table(df)

root = tb.Window(themename="darkly")
root.title("Job Tracker App")
root.geometry("1000x550")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

url_label = ttk.Label(frame, text="Job URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = ttk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = tb.Button(frame, text="Add Job", bootstyle="primary", command=add_job)
add_button.grid(row=0, column=2, padx=5, pady=5)

update_status_button = tb.Button(frame, text="Update Status", bootstyle="warning", command=update_status)
update_status_button.grid(row=1, column=0, padx=5, pady=5)

applied_button = tb.Button(frame, text="Mark as Applied", bootstyle="success", command=update_applied_date)
applied_button.grid(row=1, column=1, padx=5, pady=5)

delete_button = tb.Button(frame, text="Delete Entry", bootstyle="danger", command=delete_entry)
delete_button.grid(row=1, column=2, padx=5, pady=5)

open_excel_button = tb.Button(frame, text="Open Excel Sheet", bootstyle="secondary", command=open_excel)
open_excel_button.grid(row=1, column=3, padx=5, pady=5)

comment_button = tb.Button(frame, text="Add Comment", bootstyle="info", command=add_comment)
comment_button.grid(row=1, column=4, padx=5, pady=5)

job_table = ttk.Treeview(frame, columns=COLUMNS, show="headings")
for col in COLUMNS:
    job_table.heading(col, text=col)
    job_table.column(col, width=140)
job_table.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)

load_existing_data()
root.mainloop()