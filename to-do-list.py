import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkfont
from tkinter import ttk
import json
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")

        # Define colors
        self.bg_color = "#f5f5f5"
        self.title_color = "#3b3b3b"
        self.button_color = "#007bff"
        self.delete_button_color = "#dc3545"
        self.edit_button_color = "#ffc107"

        # Set the background color
        self.root.configure(bg=self.bg_color)

        # Set up the GUI elements
        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        # Title label with a custom font
        title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        title_label = tk.Label(self.root, text="My To-Do List", font=title_font, fg=self.title_color, bg=self.bg_color)
        title_label.pack(pady=10)

        # Frame for the listbox and scrollbar
        frame = tk.Frame(self.root, bg=self.bg_color) 
        frame.pack(pady=10)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox with custom font
        listbox_font = tkfont.Font(family="Arial", size=12)
        self.listbox = tk.Listbox(frame, width=50, height=15, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE, font=listbox_font, bg="#ffffff", fg="#333333", selectbackground=self.button_color, selectforeground="white")
        self.listbox.pack(padx=10, pady=10)
        self.scrollbar.config(command=self.listbox.yview)

        # Entry box with custom font
        entry_font = tkfont.Font(family="Arial", size=12)
        self.entry = tk.Entry(self.root, width=38, font=entry_font)
        self.entry.pack(pady=5)

        # Category and Priority dropdowns
        self.category_var = tk.StringVar(value="Personal")
        self.priority_var = tk.StringVar(value="Medium")

        category_label = tk.Label(self.root, text="Category", bg=self.bg_color)
        category_label.pack()
        category_dropdown = ttk.Combobox(self.root, textvariable=self.category_var, values=["Personal", "Work", "Others"], width=37)
        category_dropdown.pack(pady=5)

        priority_label = tk.Label(self.root, text="Priority", bg=self.bg_color)
        priority_label.pack()
        priority_dropdown = ttk.Combobox(self.root, textvariable=self.priority_var, values=["Low", "Medium", "High"], width=37)
        priority_dropdown.pack(pady=5)

        # Buttons with custom colors
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=5)

        add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, width=12, bg=self.button_color, fg="white", font=("Arial", 12, "bold"), relief="flat")
        add_button.grid(row=0, column=0, padx=5)
        add_button.bind("<Enter>", lambda e: add_button.config(bg=self.button_color, fg="white"))
        add_button.bind("<Leave>", lambda e: add_button.config(bg=self.button_color))

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, width=12, bg=self.delete_button_color, fg="white", font=("Arial", 12, "bold"), relief="flat")
        delete_button.grid(row=0, column=1, padx=5)
        delete_button.bind("<Enter>", lambda e: delete_button.config(bg="#c82333"))
        delete_button.bind("<Leave>", lambda e: delete_button.config(bg=self.delete_button_color))

        edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, width=12, bg=self.edit_button_color, fg="black", font=("Arial", 12, "bold"), relief="flat")
        edit_button.grid(row=0, column=2, padx=5)
        edit_button.bind("<Enter>", lambda e: edit_button.config(bg="#e0a800"))
        edit_button.bind("<Leave>", lambda e: edit_button.config(bg=self.edit_button_color))

    def add_task(self):
        task = self.entry.get()
        category = self.category_var.get()
        priority = self.priority_var.get()
        if task:
            task_details = f"{task} [Category: {category}, Priority: {priority}]"
            self.listbox.insert(tk.END, task_details)
            self.entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def edit_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            current_task = self.listbox.get(selected_index)
            task, details = current_task.split(' [')
            details = details.rstrip(']')
            new_task = simpledialog.askstring("Edit Task", "Update your task:", initialvalue=task)
            if new_task:
                new_details = simpledialog.askstring("Edit Details", "Update category and priority (e.g., Category: Personal, Priority: Medium):", initialvalue=details)
                if new_details:
                    new_task_details = f"{new_task} [{new_details}]"
                    self.listbox.delete(selected_index)
                    self.listbox.insert(selected_index, new_task_details)
                    self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                tasks = json.load(f)
            for task in tasks:
                self.listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

