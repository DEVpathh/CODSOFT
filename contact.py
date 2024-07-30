import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x500")
        self.root.configure(bg="#e9ecef")

        # Initialize contact list
        self.contacts = []

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_font = tkfont.Font(family="Segoe UI", size=20, weight="bold")
        title_label = tk.Label(self.root, text="Contact Book", font=title_font, bg="#e9ecef", fg="#343a40")
        title_label.pack(pady=10)

        # Input frame
        input_frame = tk.Frame(self.root, bg="#e9ecef")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Name:", bg="#e9ecef").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(input_frame, width=30, font=("Segoe UI", 12))
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Phone:", bg="#e9ecef").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(input_frame, width=30, font=("Segoe UI", 12))
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.root, bg="#e9ecef")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add Contact", command=self.add_contact, font=("Segoe UI", 12), bg="#28a745", fg="white", relief="flat")
        add_button.pack(side="left", padx=5)

        edit_button = tk.Button(button_frame, text="Edit Contact", command=self.edit_contact, font=("Segoe UI", 12), bg="#ffc107", fg="black", relief="flat")
        edit_button.pack(side="left", padx=5)

        delete_button = tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, font=("Segoe UI", 12), bg="#dc3545", fg="white", relief="flat")
        delete_button.pack(side="left", padx=5)

        search_button = tk.Button(button_frame, text="Search Contact", command=self.search_contact, font=("Segoe UI", 12), bg="#007bff", fg="white", relief="flat")
        search_button.pack(side="left", padx=5)

        # Contact listbox
        self.contact_listbox = tk.Listbox(self.root, width=50, height=15, font=("Segoe UI", 12))
        self.contact_listbox.pack(pady=10)

        # Number of contacts label
        self.num_contacts_label = tk.Label(self.root, text="", font=("Segoe UI", 12), bg="#e9ecef")
        self.num_contacts_label.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Both fields are required!")
            return

        contact = f"Name: {name}, Phone: {phone}"
        self.contacts.append(contact)
        self.update_contact_list()

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def edit_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No contact selected!")
            return
        
        old_contact = self.contacts[selected_index[0]]
        old_name, old_phone = [item.split(": ")[1] for item in old_contact.split(", ")]

        new_name = simpledialog.askstring("Edit Contact", "Enter new name:", initialvalue=old_name)
        if new_name is None: return

        new_phone = simpledialog.askstring("Edit Contact", "Enter new phone:", initialvalue=old_phone)
        if new_phone is None: return

        self.contacts[selected_index[0]] = f"Name: {new_name}, Phone: {new_phone}"
        self.update_contact_list()

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No contact selected!")
            return
        
        self.contacts.pop(selected_index[0])
        self.update_contact_list()

    def search_contact(self):
        search_query = simpledialog.askstring("Search", "Enter name or part of the contact to search:")
        if search_query:
            search_results = [contact for contact in self.contacts if search_query.lower() in contact.lower()]
            if search_results:
                self.contact_listbox.delete(0, tk.END)
                for result in search_results:
                    self.contact_listbox.insert(tk.END, result)
            else:
                messagebox.showinfo("Search Results", "No contacts found!")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact)
        self.num_contacts_label.config(text=f"Number of Contacts: {len(self.contacts)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

