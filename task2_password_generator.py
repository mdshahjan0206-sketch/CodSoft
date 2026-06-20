import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        result_label.config(text=password)

    except ValueError:
        result_label.config(text="Enter a valid number!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

tk.Label(root, text="Password Generator",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password",
          command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="", wraplength=350)
result_label.pack(pady=10)

root.mainloop()
