# Import tkinter module for GUI
import tkinter as tk

# Import random module to generate random characters
import random

# Import string module to get letters, digits, and symbols
import string

# Function to generate password
def generate_password():
    try:
        # Get password length from entry box
        length = int(length_entry.get())

        # Combine uppercase, lowercase, digits, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate random password of specified length
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display generated password on label
        result_label.config(text=password)

    except ValueError:
        # Display error if user enters invalid input
        result_label.config(text="Enter a valid number!")

# Create main application window
root = tk.Tk()

# Set window title
root.title("Password Generator")

# Set window size
root.geometry("400x250")

# Create heading label
tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 16, "bold")
).pack(pady=10)


# Create label asking for password length
tk.Label(
    root,
    text="Enter Password Length"
).pack()

# Create input box for length
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Create button to generate password
tk.Button(
    root,
    text="Generate Password",
    command=generate_password
).pack(pady=10)

# Label to display generated password
result_label = tk.Label(
    root,
    text="",
    wraplength=350
)
result_label.pack(pady=10)


# Run the application
root.mainloop()
