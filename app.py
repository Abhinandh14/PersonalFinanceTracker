import tkinter as tk

root = tk.Tk()
root.title("Personal Finance Tracker")

# Set the background color
root.configure(background="#f2f2f2")

# Create a label with a custom font and color
label = tk.Label(root, text="Personal Finance Tracker", font=("Arial", 24), fg="#00698f")
label.pack(pady=20)

# Create a button with a custom background color and font
button = tk.Button(root, text="Add Transaction", bg="#4CAF50", font=("Arial", 18), fg="#ffffff")
button.pack(pady=10)

# Create a frame to hold the main components
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Create the frames for the different sections of the application
frame_header = tk.Frame(root)
frame_content = tk.Frame(root)
frame_footer = tk.Frame(root)

# Pack the frames into the main window
frame_header.pack(fill="x")
frame_content.pack(fill="both", expand=True)
frame_footer.pack(fill="x")

# Create a label and text field for the user to enter their income
income_label = tk.Label(main_frame, text="Income:")
income_label.pack()
income_text = tk.Entry(main_frame)
income_text.pack()

# Create a label and text field for the user to enter their expenses
expenses_label = tk.Label(main_frame, text="Expenses:")
expenses_label.pack()
expenses_text = tk.Entry(main_frame)
expenses_text.pack()

# Create the labels and buttons for the header frame
label_header = tk.Label(frame_header, text="Personal Finance Tracker")
button_add_transaction = tk.Button(frame_header, text="Add Transaction")

# Pack the labels and buttons into the header frame
label_header.pack(side="left")
button_add_transaction.pack(side="right")

# Create the labels and entry fields for the content frame
label_date = tk.Label(frame_content, text="Date:")
entry_date = tk.Entry(frame_content)
label_amount = tk.Label(frame_content, text="Amount:")
entry_amount = tk.Entry(frame_content)

# Pack the labels and entry fields into the content frame
label_date.grid(row=0, column=0)
entry_date.grid(row=0, column=1)
label_amount.grid(row=1, column=0)
entry_amount.grid(row=1, column=1)

root.mainloop()