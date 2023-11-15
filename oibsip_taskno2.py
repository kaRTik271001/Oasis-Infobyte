import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    """
    Calculate BMI using the weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height * height)
    """
    return weight / (height ** 2)

def interpret_bmi(bmi):
    """
    Interpret BMI and provide a basic classification.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_button_click():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Interpret BMI
        interpretation = interpret_bmi(bmi)

        # Display the result
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nInterpretation: {interpretation}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
weight_label = tk.Label(root, text="Enter weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter height (m):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_button_click)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()