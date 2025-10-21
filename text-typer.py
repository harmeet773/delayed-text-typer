import tkinter as tk
from tkinter import ttk
import pyautogui

# Create GUI window
root = tk.Tk()
root.title("Text Typer")

# Define a larger font
my_font = ("Helvetica", 14)

def delayed_typing():
    try:
        seconds = int(spinbox.get())
    except ValueError:
        result_label.config(text="Please enter a valid number")
        return

    text1 = text_entry.get().strip()
    if not text1:
        result_label.config(text="Please enter some text.")
        return

    result_label.config(text=f"Waiting for {seconds} second(s)...")

    # Disable buttons during waiting period
    start_button.config(state='disabled')
    clear_button.config(state='disabled')

    # Countdown display
    def countdown(remaining):
        if remaining > 0:
            result_label.config(text=f"Typing in {remaining}...")
            root.after(1000, countdown, remaining - 1)
        else:
            result_label.config(text="Typing now...")
            pyautogui.write(text1, interval=0.05)
            result_label.config(text="Text has been typed!")
            start_button.config(state='normal')
            clear_button.config(state='normal')
    # Start countdown
    countdown(seconds)

def clear_text():
    text_entry.delete(0, tk.END)
    result_label.config(text="Text box cleared.")

# Label and Entry for text
ttk.Label(root, text="Provide your text below:", font=my_font).pack(pady=10)
text_entry = ttk.Entry(root, width=50, font=my_font)
text_entry.pack(pady=5)
text_entry.focus_set()

# Spinbox for numeric input (seconds)
spin_label = ttk.Label(root, text=f"Start typing after {3} seconds:", font=my_font)
spin_label.pack(pady=10)

spinbox = ttk.Spinbox(root, from_=1, to=3600, width=10, font=my_font)
spinbox.set(3)
spinbox.pack(pady=5)

# Update the label whenever spinbox value changes
def update_spin_label(*args):
    spin_label.config(text=f"Start typing after {spinbox.get()} seconds:")

spinbox.bind("<<Increment>>", update_spin_label)
spinbox.bind("<<Decrement>>", update_spin_label)
spinbox.bind("<KeyRelease>", update_spin_label)

# Buttons
style = ttk.Style()
style.configure('Large.TButton', font=my_font)

start_button = ttk.Button(root, text="Start Typing", command=delayed_typing, style='Large.TButton')
start_button.pack(pady=10)

clear_button = ttk.Button(root, text="Clear Text", command=clear_text, style='Large.TButton')
clear_button.pack(pady=5)

# Status label
result_label = ttk.Label(root, text="", font=my_font)
result_label.pack(pady=5)

# Author details
author_label = ttk.Label(
    root,
    text="Author: Harmeet Singh Chugga",
    font=(*my_font, "bold")
)
# pady - “padding in the y-direction”, pady = (x,y) -> add x pixels above and y pixels below 
author_label.pack(pady=(15,0))

linkedin_label = ttk.Label(
    root,
    text="LinkedIn: www.linkedin.com/in/harmeet-singh-chugga",
    font=("Helvetica", 10),
    foreground="blue",
    cursor="hand2"
)
linkedin_label.pack(pady=(0, 10))

# Make the LinkedIn label clickable
def open_linkedin(event):
    import webbrowser
    webbrowser.open_new("https://www.linkedin.com/in/harmeet-singh-chugga")

linkedin_label.bind("<Button-1>", open_linkedin)


# Instruction label
instruction_label = ttk.Label(root, text="Press ESC to close the app", font=("Helvetica", 10, "italic"))
instruction_label.pack(side='bottom', fill='x', pady=5)

# Escape key to close app
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()
