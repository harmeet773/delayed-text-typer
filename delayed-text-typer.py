import tkinter as tk
from tkinter import ttk
import pyautogui

# Create GUI window
root = tk.Tk()
root.title("Delayed Text Typer")
root.geometry("600x300")  # Increased window size

# Define a larger font
LARGE_FONT = ("Helvetica", 14)

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

    # Countdown display (optional)
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
ttk.Label(root, text="Text Box:", font=LARGE_FONT).pack(pady=10)
text_entry = ttk.Entry(root, width=50, font=LARGE_FONT)
text_entry.pack(pady=5)
text_entry.focus_set()

# Label and Spinbox for numeric input (seconds)
ttk.Label(root, text="Delay (in seconds):", font=LARGE_FONT).pack(pady=10)
spinbox = ttk.Spinbox(root, from_=1, to=3600, width=10, font=LARGE_FONT)
spinbox.set(3)
spinbox.pack(pady=5)

# Buttons
start_button = ttk.Button(root, text="Start Typing", command=delayed_typing)
start_button.pack(pady=10)
start_button.configure(style='Large.TButton')

clear_button = ttk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack(pady=5)
clear_button.configure(style='Large.TButton')

# Status label
result_label = ttk.Label(root, text="", font=LARGE_FONT)
result_label.pack(pady=5)

# Style configuration for larger button font
style = ttk.Style()
style.configure('Large.TButton', font=LARGE_FONT)

# Optional: Escape key to close app
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()
