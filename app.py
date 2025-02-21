

import tkinter as tk
from datetime import date
from tkinter import messagebox
from transaction import FinancialTransaction

class FinanceTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Personal Finance Tracker")
        self.window.geometry("600x500")
        self.transactions = []
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
        transaction_window.geometry("300x300")

        label_date = tk.Label(transaction_window, text="Date (YYYY-MM-DD):")
        label_date.pack(pady=5)
        entry_date = tk.Entry(transaction_window)
        entry_date.pack(pady=5)

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
                                command=lambda: self.save_transaction(entry_date.get(), entry_amount.get(), entry_category.get(), entry_description.get(), transaction_window))
        button_save.pack(pady=10)

    def calculate_total(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.amount
        return total

    def categorize_transactions(self):
        categorized_transactions = {}
        for transaction in self.transactions:
            if transaction.category not in categorized_transactions:
                categorized_transactions[transaction.category] = []
            categorized_transactions[transaction.category].append(transaction)
        return categorized_transactions
    
    def save_transaction(self, transaction_date, amount, category, description, window):
        # 
        try:
            #amount = float(amount)
            # Create a temp transaction object to validate data
            transaction = FinancialTransaction(transaction_date, float(amount), category, description)

            if not transaction.validate_date(transaction_date):
                raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

            if not transaction.validate_amount(float(amount)):
                raise ValueError("Amount should be a positive number.")

            if not transaction.validate_category(category):
                raise ValueError("Invalid category. Use 'income', 'expense', or 'transfer'.")

            if not transaction.validate_description(description):
                raise ValueError("Description cannot be empty.")

            #transaction = FinancialTransaction(transaction_date, float(amount), category, description)
            # If all validations pass, add the transaction
            self.transactions.append(transaction)
            print(f"Transaction Saved: {transaction.transaction_date}, {transaction.amount}, {transaction.category}, {transaction.description}")
            messagebox.showinfo("Transaction Saved", f"Transaction of {transaction.amount} added successfully!", parent=window)
            window.destroy()
        except ValueError as e:  # Catch the specific error message
            window.lift()  
            window.focus_force()
            messagebox.showerror("Invalid Input", str(e), parent=window)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = FinanceTracker()
    app.run()