import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Password Generator")
        self.root.geometry("500x400")
        self.root.configure(bg="#ffffff")

        # Create the GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_font = tkfont.Font(family="Arial", size=20, weight="bold")
        title_label = tk.Label(self.root, text="Password Generator", font=title_font, bg="#ffffff", fg="#333333")
        title_label.pack(pady=20)

        # Password length label and entry
        length_frame = tk.Frame(self.root, bg="#ffffff")
        length_frame.pack(pady=(10, 0))

        length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#ffffff", fg="#333333")
        length_label.pack(side=tk.LEFT, padx=10)

        self.length_var = tk.IntVar(value=12)
        length_entry = tk.Entry(length_frame, textvariable=self.length_var, width=5, font=("Arial", 12), justify='center')
        length_entry.pack(side=tk.LEFT, padx=10)

        # Options for including different characters
        options_frame = tk.Frame(self.root, bg="#ffffff")
        options_frame.pack(pady=(10, 0))

        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        tk.Checkbutton(options_frame, text="Include Uppercase Letters", variable=self.include_uppercase, font=("Arial", 12), bg="#ffffff", fg="#333333").pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text="Include Lowercase Letters", variable=self.include_lowercase, font=("Arial", 12), bg="#ffffff", fg="#333333").pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text="Include Digits", variable=self.include_digits, font=("Arial", 12), bg="#ffffff", fg="#333333").pack(anchor=tk.W, padx=10)
        tk.Checkbutton(options_frame, text="Include Special Characters", variable=self.include_special, font=("Arial", 12), bg="#ffffff", fg="#333333").pack(anchor=tk.W, padx=10)

        # Generate button
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=20)

        generate_button = tk.Button(button_frame, text="Generate Password", command=self.generate_password, font=("Arial", 12, "bold"), bg="#007bff", fg="white", relief="flat")
        generate_button.pack()

        # Password display
        result_frame = tk.Frame(self.root, bg="#ffffff")
        result_frame.pack(pady=(20, 0))

        password_label = tk.Label(result_frame, text="Generated Password:", font=("Arial", 12), bg="#ffffff", fg="#333333")
        password_label.pack(anchor=tk.W)

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(result_frame, textvariable=self.password_var, width=60, font=("Arial", 12), state="readonly")
        self.password_entry.pack(pady=(0, 10))

        copy_button = tk.Button(result_frame, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 12, "bold"), bg="#28a745", fg="white", relief="flat")
        copy_button.pack()

        # Password strength indicator
        self.strength_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#ffffff")
        self.strength_label.pack(pady=(10, 0))

    def generate_password(self):
        length = self.length_var.get()
        if length < 1:
            messagebox.showwarning("Invalid Length", "Password length must be at least 1.")
            return

        chars = ""
        if self.include_uppercase.get():
            chars += string.ascii_uppercase
        if self.include_lowercase.get():
            chars += string.ascii_lowercase
        if self.include_digits.get():
            chars += string.digits
        if self.include_special.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("No Characters Selected", "You must select at least one character type.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)
        self.evaluate_password_strength(password)

    def evaluate_password_strength(self, password):
        length = len(password)
        strength, color = "Weak", "red"
        if length >= 12:
            if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
                if any(c in string.punctuation for c in password):
                    strength, color = "Strong", "green"
                else:
                    strength, color = "Moderate", "orange"
            else:
                strength, color = "Moderate", "orange"
        self.strength_label.config(text=f"Password Strength: {strength}", fg=color)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
