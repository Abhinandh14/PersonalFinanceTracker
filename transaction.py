from datetime import datetime

class FinancialTransaction:
    def __init__(self, transaction_date, amount, category, description):
        self.transaction_date = transaction_date
        self.amount = amount
        self.category = category
        self.description = description

    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_amount(self, amount):
        try:
            amount = float(amount)  # Convert to float first
            return amount > 0
        except ValueError:
            return False

    def validate_category(self, category):
        # Define a list of valid categories
        valid_categories = ['income', 'expense', 'transfer']
        if category not in valid_categories:
            return False
        return True

    def validate_description(self, description):
        if len(description) == 0:
            return False
        return True

    # def add_transaction(self, transaction_date, amount, category, description):
    #     if self.validate_date(transaction_date) and self.validate_amount(amount) and self.validate_category(category) and self.validate_description(description):
    #         # Add the transaction to the list of transactions
    #         print("Transaction added successfully")
    #     else:
    #         print("Invalid transaction data")

