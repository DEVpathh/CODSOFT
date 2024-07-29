import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Entry for adding new tasks
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Button to add the task
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=100, height=10)
        self.task_listbox.pack(pady=10)

        # Button to remove selected task
        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
