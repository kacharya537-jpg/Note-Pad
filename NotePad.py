import tkinter as tk
from tkinter import filedialog, messagebox
import time

# --- APP SETUP ---
root = tk.Tk()
root.title("8-Bit Editor")
root.geometry("700x500")
root.configure(bg="#0f380f")

FONT = ("Courier", 11, "bold")

# --- BOOT SCREEN ---
boot_frame = tk.Frame(root, bg="#0f380f")
boot_label = tk.Label(
    boot_frame,
    text="BOOTING 8-BIT EDITOR...\n\n[##########]",
    fg="#9bbc0f",
    bg="#0f380f",
    font=("Courier", 14, "bold"),
    justify="center"
)
boot_label.pack(expand=True)

boot_frame.pack(expand=True, fill="both")
root.update()
time.sleep(1.5)
boot_frame.destroy()

# --- MAIN UI ---
# Menu bar
menu_bar = tk.Menu(root, bg="#306230", fg="white", tearoff=0)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0, bg="#306230", fg="white")
edit_menu = tk.Menu(menu_bar, tearoff=0, bg="#306230", fg="white")

menu_bar.add_cascade(label="FILE", menu=file_menu)
menu_bar.add_cascade(label="EDIT", menu=edit_menu)

# ,-- Text Area -->
text_area = tk.Text(
    root,
    wrap="word",
    font=FONT,
    bg="#0f380f",
    fg="#9bbc0f",
    insertbackground="white",
    borderwidth=6,
    relief="ridge"
)
text_area.pack(expand=True, fill="both", padx=10, pady=5)

# <--- Status Bar --->
status = tk.Label(
    root,
    text="READY",
    anchor="w",
    bg="#306230",
    fg="white",
    font=("Courier", 9, "bold")
)
status.pack(fill="x")

# <--- Functions Creation --->
current_file = None

def update_status(msg):
    status.config(text=msg)
    root.update()

def new_file():
    global current_file
    text_area.delete(1.0, tk.END)
    current_file = None
    update_status("NEW FILE")

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        current_file = file_path
        update_status(f"OPENED: {file_path}")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        update_status("SAVED")
    else:
        save_as()

def save_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        current_file = file_path
        save_file()

def exit_app():
    if messagebox.askyesno("EXIT", "Quit editor?"):
        root.destroy()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

# <--- Functions --->
