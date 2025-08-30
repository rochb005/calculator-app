import tkinter as tk
from tkinter import ttk

def handle_button_click(clicked_button_text):
    current_text = result_var.get()
    if clicked_button_text == "=":
        try:
            # Replace custom symbols with Python operators
            expression = current_text.replace("÷", "/").replace("×", "*")
            result = eval(expression)
            # Check if the result is a whole number
            if result.is_integer():
                result = int(result)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif clicked_button_text == "C":
        result_var.set("")
    elif clicked_button_text == "%":
        # Convert the current number to a decimal by dividing it by 100
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")
    elif clicked_button_text == "±":
        # Convert the current number to its negative
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")
    else:
        result_var.set(current_text + clicked_button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set the background color to burgundy (酒红色)
root.configure(bg="#800020")

# Create a frame for the calculator with burgundy border
calc_frame = tk.Frame(root, bg="#800020", bd=20, relief=tk.RAISED)
calc_frame.pack(padx=10, pady=10)

# Entry widget to display the result with larger font size
result_var = tk.StringVar()
result_entry = tk.Entry(calc_frame, textvariable=result_var, font=("Helvetica", 24), 
                        justify="right", bg="white", fg="black", bd=0, highlightthickness=0)
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Button layout
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

# Define colors for buttons
button_colors = {
    # First row: pink and orange
    "C": {"bg": "#FFB6C1", "fg": "black"},  # Light pink
    "±": {"bg": "#FFA500", "fg": "white"},  # Orange
    "%": {"bg": "#FFA500", "fg": "white"},  # Orange
    "÷": {"bg": "#FFA500", "fg": "white"},  # Orange
    
    # Second to fourth rows: white and orange
    "7": {"bg": "white", "fg": "black"},
    "8": {"bg": "white", "fg": "black"},
    "9": {"bg": "white", "fg": "black"},
    "×": {"bg": "#FFA500", "fg": "white"},  # Orange
    
    "4": {"bg": "white", "fg": "black"},
    "5": {"bg": "white", "fg": "black"},
    "6": {"bg": "white", "fg": "black"},
    "-": {"bg": "#FFA500", "fg": "white"},  # Orange
    
    "1": {"bg": "white", "fg": "black"},
    "2": {"bg": "white", "fg": "black"},
    "3": {"bg": "white", "fg": "black"},
    "+": {"bg": "#FFA500", "fg": "white"},  # Orange
    
    # Last row: white, light pink, and orange
    "0": {"bg": "white", "fg": "black"},    # White (long button)
    ".": {"bg": "#FFC0CB", "fg": "black"},  # Light pink
    "=": {"bg": "#FFA500", "fg": "white"}   # Orange
}

# Create buttons and add them to the grid
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    
    # Get colors for this button
    colors = button_colors.get(button_text, {"bg": "white", "fg": "black"})
    
    # Create button with specified colors
    button = tk.Button(
        calc_frame, 
        text=button_text, 
        command=lambda text=button_text: handle_button_click(text),
        bg=colors["bg"],
        fg=colors["fg"],
        font=("Helvetica", 16),
        width=5,
        height=2,
        relief=tk.RAISED,
        bd=2,
        highlightthickness=0
    )
    
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Configure row and column weights so that they expand proportionally
for i in range(6):
    calc_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    calc_frame.grid_columnconfigure(i, weight=1)

# Set the window size to a 9:16 ratio
width = 400
height = 600
root.geometry(f"{width}x{height}")

# Make the window non-resizable
root.resizable(False, False)

# Keyboard control
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<BackSpace>", lambda event: handle_button_click("C"))

# Run the main loop
root.mainloop()