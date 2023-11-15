import tkinter as tk
from tkinter import StringVar, IntVar, messagebox
import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password based on user-defined criteria.
    """
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    try:
        password_length = int(length_entry.get())
        use_letters = letters_var.get() == 1
        use_numbers = numbers_var.get() == 1
        use_symbols = symbols_var.get() == 1

        # Generate and display the password
        password = generate_password(password_length, use_letters, use_numbers, use_symbols)
        if password:
            result_var.set(f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value for password length.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    root.update()

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

letters_var = IntVar()
letters_checkbox = tk.Checkbutton(root, text="Include letters", variable=letters_var)
letters_checkbox.pack()

numbers_var = IntVar()
numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
numbers_checkbox.pack()

symbols_var = IntVar()
symbols_checkbox = tk.Checkbutton(root, text="Include symbols", variable=symbols_var)
symbols_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_click)
generate_button.pack()

result_var = StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# Start the Tkinter event loop
root.mainloop()