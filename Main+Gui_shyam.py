import tkinter as tk
from tkinter import filedialog, messagebox
from db_connect import get_signatures
import scanner
import os

selected_file_path = None
root = tk.Tk()
root.title("Neural Defender")
root.geometry("720x510")
root.configure(bg="#f5f5f5")
root.iconbitmap("Logo.ico")

header_frame = tk.Frame(root, bg="#ffffff")
header_frame.pack(fill="x", pady=(0, 5))
try:
    logo = tk.PhotoImage(file="Logo_small.png") 
    logo_label = tk.Label(header_frame, image=logo, bg="#ffffff")
    logo_label.image = logo
    logo_label.pack(side="left", padx=(15, 5), pady=5)
except Exception as e:
    print(f"Logo load failed: {e}")

title_label = tk.Label(
    header_frame,
    text="Neural Defender",
    font=("Helvetica", 22, "bold"),
    bg="#ffffff",
    fg="#000"
)
title_label.pack(side="left", pady=5)

# --- MAIN CONTENT AREA ---
main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

left_frame = tk.Frame(main_frame, bg="#f5f5f5")
left_frame.grid(row=0, column=0, padx=20, pady=10, sticky="n")

file_label = tk.Label(
    left_frame,
    text="No file selected",
    font=("Helvetica", 10, "italic"),
    bg="#f5f5f5",
    fg="#555"
)
file_label.pack(pady=5)

def select_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a file to scan")
    if not file_path:
        return
    selected_file_path = file_path
    file_name = os.path.basename(file_path)
    file_label.config(text=f"Selected: {file_name}")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"File selected: {file_name}\nClick 'File Upload' to start scanning.\n")

def start_scan():
    global selected_file_path
    if not selected_file_path:
        messagebox.showwarning("No File", "Please select a file before scanning.")
        return
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Scanning file: {os.path.basename(selected_file_path)}...\n\n")
    try:
        signatures = get_signatures()
        result = scanner.scan_file(selected_file_path, signatures)
        output_text.insert(tk.END, f"{result}\n")
        if "INFECTED" in result.upper():
            status_label.config(text=" INFECTED", fg="red")
            os.remove(f"{selected_file_path}")
        elif "SAFE" in result.upper():
            status_label.config(text=" SAFE", fg="green")
        else:
            status_label.config(text=" Unknown", fg="orange")
    except Exception as e:
        status_label.config(text=" ERROR", fg="red")
        output_text.insert(tk.END, f" Error: {e}")
        

def help_popup():
    messagebox.showinfo(
        "Help",
        "How to Use Neural Defender:\n\n"
        "1️ Click 'Select File' to choose the file you want to scan.\n"
        "2️ The selected file name will appear above the buttons.\n"
        "3️ Click 'Scan' to start the scan.\n"
        "4️ Results will be displayed in the output window."
    )
def support_btn():
     messagebox.showinfo(
        "Support",
        "Contact the Developers -:\n\n"
        "Name     Branch\n\n"
        "Aditya - AI&DS \n"
        "Paras -  AI&DS \n"
        "Shyam -  AI&DS \n"
        "Domain - Ai&DS"
     )

select_btn = tk.Button(
    left_frame, text="Select File", font=("Helvetica", 12, "bold"),
    width=20, height=2, bg="#e0e0e0", command=select_file
)
select_btn.pack(pady=10)
upload_btn = tk.Button(
    left_frame, text="Scan", font=("Helvetica", 12, "bold"),
    width=20, height=2, bg="#e0e0e0", command=start_scan
)
upload_btn.pack(pady=15)

right_frame = tk.Frame(main_frame, bg="#f5f5f5")
right_frame.grid(row=0, column=1, padx=20, pady=12, sticky="n")

output_label = tk.Label(
    right_frame, text="Scan Output",
    font=("Helvetica", 14, "bold"),
    bg="#f5f5f5"
)
output_label.pack(anchor="w")

output_text = tk.Text(
    right_frame, width=50, height=15,
    bg="#e8e8e8", fg="#000", wrap="word", relief="flat"
)
output_text.pack(pady=10)

status_label = tk.Label(
    right_frame, text="",
    font=("Helvetica", 14, "bold"),
    bg="#f5f5f5"
)
status_label.pack(pady=5)

help_btn = tk.Button(
    root, text="Help", font=("Helvetica", 11, "bold"),
    bg="#1a2a3a", fg="white", command=help_popup
)
help_btn.place(x=620, y=450)

support_btn = tk.Button(
    root, text="Support", font=("Helvetica", 11, "bold"),
    bg="#2bb6b6", fg="white", command=support_btn
)
support_btn.place(x=605, y=38)

footer_label = tk.Label(
    root,
    text="Made by Neural Defender Team -: Aditya,Domain,Shyam,Paras",
    font=("Helvetica", 10, "italic"),
    bg="#f5f5f5",
    fg="#333"
)
footer_label.place(x=20, y=470)

root.mainloop()
