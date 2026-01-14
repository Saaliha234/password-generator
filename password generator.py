import tkinter as tk
from tkinter import messagebox 
import random
import string


def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showwarning("Weak Length", "Password length should be at least 6")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid length")
        return

    chars = ""
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Error", "Select at least one option")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

    check_strength(password)

def check_strength(password):
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    strength = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    label_strength.config(text=f"Strength: {strength[score-1]}", fg="green" if score >= 4 else "orange")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")


root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x450")

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)


tk.Label(root, text="Password Length").pack()
entry_length = tk.Entry(root)
entry_length.insert(0, "12")
entry_length.pack()


var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase Letters (A-Z)", variable=var_upper).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Lowercase Letters (a-z)", variable=var_lower).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Numbers (0-9)", variable=var_digits).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Symbols (!@#$%)", variable=var_symbols).pack(anchor="w", padx=50)


tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)


entry_password = tk.Entry(root, font=("Arial", 12), justify="center")
entry_password.pack(pady=5)


label_strength = tk.Label(root, text="Strength: ")
label_strength.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)


tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()


