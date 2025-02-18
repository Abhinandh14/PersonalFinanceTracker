import tkinter as tk
from tkinter import ttk

# Create a simple tkinter window
root = tk.Tk()
root.title("Test Tkinter")

# Create a label
label = ttk.Label(root, text="Tkinter is working")
label.pack()

# Start the tkinter event loop
root.mainloop()