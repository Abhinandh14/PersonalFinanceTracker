# import tkinter as tk

# root = tk.Tk()
# root.title("Personal Finance Tracker")

# # Set the background color
# root.configure(background="#f2f2f2")

# # Create a label with a custom font and color
# label = tk.Label(root, text="Personal Finance Tracker", font=("Arial", 24), fg="#00698f")
# label.pack(pady=20)

# # Create a frame to hold the main components
# main_frame = tk.Frame(root)
# main_frame.pack(fill="both", expand=True)

# # Create a label and text field for the user to enter their income
# income_label = tk.Label(main_frame, text="Income:")
# income_label.pack()
# income_text = tk.Entry(main_frame)
# income_text.pack()

# # Create a label and text field for the user to enter their expenses
# expenses_label = tk.Label(main_frame, text="Expenses:")
# expenses_label.pack()
# expenses_text = tk.Entry(main_frame)
# expenses_text.pack()



# # The code creates a main frame to hold the components of the application, including labels and text fields for the user to enter their income and expenses. The components are packed into the main frame using the pack() method. The main frame is then packed into the main window using the pack() method. Finally, the main window enters the main event loop using the mainloop() method.


# # Create the frames for the different sections of the application
# frame_header = tk.Frame(root)
# frame_content = tk.Frame(root)
# frame_footer = tk.Frame(root)

# # Pack the frames into the main window
# frame_header.pack(fill="x")
# frame_content.pack(fill="both", expand=True)
# frame_footer.pack(fill="x")



# # Create the labels and buttons for the header frame
# label_header = tk.Label(frame_header, text="Personal Finance Tracker")
# button_add_transaction = tk.Button(frame_header, text="Add Transaction")

# # Pack the labels and buttons into the header frame
# label_header.pack(side="left")
# button_add_transaction.pack(side="right")

# # Create the labels and entry fields for the content frame
# label_date = tk.Label(frame_content, text="Date:")
# entry_date = tk.Entry(frame_content)
# label_amount = tk.Label(frame_content, text="Amount:")
# entry_amount = tk.Entry(frame_content)

# # Pack the labels and entry fields into the content frame
# label_date.grid(row=0, column=0)
# entry_date.grid(row=0, column=1)
# label_amount.grid(row=1, column=0)
# entry_amount.grid(row=1, column=1)






# # Create a button with a custom background color and font
# button = tk.Button(root, text="Add Transaction", bg="#4CAF50", font=("Arial", 18), fg="#ffffff")
# button.pack(pady=10)

# root.mainloop()

import tkinter as tk
from datetime import date
from tkinter import messagebox
from transaction import FinancialTransaction

class FinanceTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Personal Finance Tracker")
        self.window.geometry("600x500")
        self.create_main_ui()
        
    def create_main_ui(self):
        # Header Frame
        frame_header = tk.Frame(self.window)
        frame_header.pack(fill="x")
        label_header = tk.Label(frame_header, text="Personal Finance Tracker", font=("Arial", 24), fg="#00698f")
        label_header.pack(side="left", padx=10, pady=10)
        
        # button_add_transaction = tk.Button(frame_header, text="Add Transaction", command=self.add_transaction)
        # button_add_transaction.pack(side="right", padx=10)
        button_add = tk.Button(frame_header, text="Add Transaction", bg="#4CAF50", font=("Arial", 18), fg="#ffffff", command=self.add_transaction)
        button_add.pack(pady=10)

#         # Create the labels and entry fields for the content frame
#         label_date = tk.Label(frame_content, text="Date:")
#         entry_date = tk.Entry(frame_content)
#         label_amount = tk.Label(frame_content, text="Amount:")
#         entry_amount = tk.Entry(frame_content)

#         # Pack the labels and entry fields into the content frame
#     label_date.grid(row=0, column=0)
# entry_date.grid(row=0, column=1)
# label_amount.grid(row=1, column=0)
# entry_amount.grid(row=1, column=1)

        # Content Frame
        frame_content = tk.Frame(self.window)
        frame_content.pack(fill="both", expand=True)

        label_income = tk.Label(frame_content, text="Income:")
        label_income.grid(row=0, column=0, padx=10, pady=5)
        self.entry_income = tk.Entry(frame_content)
        self.entry_income.grid(row=0, column=1, padx=10, pady=5)
        
        label_expenses = tk.Label(frame_content, text="Expenses:")
        label_expenses.grid(row=1, column=0, padx=10, pady=5)
        self.entry_expenses = tk.Entry(frame_content)
        self.entry_expenses.grid(row=1, column=1, padx=10, pady=5)

        # Footer Frame
        frame_footer = tk.Frame(self.window)
        frame_footer.pack(fill="x", pady=10)
        # button_add = tk.Button(frame_footer, text="Add Transaction", bg="#4CAF50", font=("Arial", 18), fg="#ffffff", command=self.add_transaction)
        # button_add.pack()
    
    def add_transaction(self):
        transaction_window = tk.Toplevel(self.window)
        transaction_window.title("Add Transaction")
        transaction_window.geometry("300x250")
        
        label_amount = tk.Label(transaction_window, text="Transaction Amount:")
        label_amount.pack(pady=5)
        entry_amount = tk.Entry(transaction_window)
        entry_amount.pack(pady=5)

        label_category = tk.Label(transaction_window, text="Category:")
        label_category.pack(pady=5)
        entry_category = tk.Entry(transaction_window)
        entry_category.pack(pady=5)
        
        label_description = tk.Label(transaction_window, text="Description:")
        label_description.pack(pady=5)
        entry_description = tk.Entry(transaction_window)
        entry_description.pack(pady=5)

        # button_save = tk.Button(transaction_window, text="Save", command=lambda: self.save_transaction(entry_amount.get()))
        # button_save.pack(pady=10)
        button_save = tk.Button(transaction_window, text="Save", bg="#4CAF50", fg="white", font=("Arial", 14),
                                command=lambda: self.save_transaction(entry_amount.get(), entry_category.get(), entry_description.get(), transaction_window))
        button_save.pack(pady=10)
    
    def save_transaction(self, amount, category, description, window):
        # 
        try:
            transaction = FinancialTransaction(date.today(), float(amount), category, description)
            print(f"Transaction Saved: {transaction.transaction_date}, {transaction.amount}, {transaction.category}, {transaction.description}")
            messagebox.showinfo("Transaction Saved", f"Transaction of {transaction.amount} added successfully!")
            window.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = FinanceTracker()
    app.run()