import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Length label and entry
        tk.Label(self.root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.length_var = tk.IntVar(value=12)
        tk.Spinbox(self.root, from_=6, to_=24, textvariable=self.length_var, width=5).grid(row=0, column=1, padx=10, pady=10)

        # Checkbox options for including characters
        self.include_uppercase = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.include_uppercase).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='w')

        self.include_digits = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')

        self.include_symbols = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')

        # Button to generate the password
        tk.Button(self.root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=10)

        # Entry to display the generated password
        self.password_entry = tk.Entry(self.root, width=40, font=('Arial', 14), bd=5)
        self.password_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        if length < 6:
            messagebox.showwarning("Warning", "Password length should be at least 6 characters.")
            return

        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "You must select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
