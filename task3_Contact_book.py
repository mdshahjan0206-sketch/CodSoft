# Import tkinter for GUI
import tkinter as tk

# Import messagebox for popup messages
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

# Function to add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Check if name field is empty
    if name == "":
        messagebox.showerror("Error", "Please enter a name!")
        return

    # Save contact
    contacts[name] = [phone, email, address]

    messagebox.showinfo("Success", "Contact Added Successfully!")

    clear_fields()
    view_contacts()


# Function to display contacts
def view_contacts():
    contact_list.delete(0, tk.END)

    for name in contacts:
        contact_list.insert(tk.END, name)


# Function to search contact
def search_contact():
    name = name_entry.get()

    if name in contacts:

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contacts[name][0])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, contacts[name][1])

        address_entry.delete(0, tk.END)
        address_entry.insert(0, contacts[name][2])

    else:
        messagebox.showerror("Error", "Contact Not Found!")


# Function to update contact
def update_contact():
    name = name_entry.get()

    if name in contacts:

        contacts[name] = [
            phone_entry.get(),
            email_entry.get(),
            address_entry.get()
        ]

        messagebox.showinfo("Success", "Contact Updated!")

        view_contacts()

    else:
        messagebox.showerror("Error", "Contact Not Found!")


# Function to delete contact
def delete_contact():
    name = name_entry.get()

    if name in contacts:

        del contacts[name]

        messagebox.showinfo("Success", "Contact Deleted!")

        clear_fields()
        view_contacts()

    else:
        messagebox.showerror("Error", "Contact Not Found!")


# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# Create main window
root = tk.Tk()

# Window title
root.title("Contact Book")

# Window size
root.geometry("600x500")

# Heading
title = tk.Label(
    root,
    text="CONTACT BOOK",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Name
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# Phone
tk.Label(root, text="Phone Number").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

# Email
tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# Address
tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
tk.Button(
    button_frame,
    text="Add",
    width=12,
    command=add_contact
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Search",
    width=12,
    command=search_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Update",
    width=12,
    command=update_contact
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    width=12,
    command=delete_contact
).grid(row=0, column=3, padx=5)

# Contact List Title
tk.Label(
    root,
    text="Saved Contacts",
    font=("Arial", 12, "bold")
).pack()

# Contact List Box
contact_list = tk.Listbox(
    root,
    width=50,
    height=10
)
contact_list.pack(pady=10)

# Start application
root.mainloop()
