import os

class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = self.generate_account_number()
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        self.create_statement_file()

    def generate_account_number(self):
        # Generate a random account number
        import random
        return random.randint(1000000000, 9999999999)

    def create_statement_file(self):
        # Create a new file to store the transaction history
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write(f"Account Number: {self.accountNumber}\n")
                file.write(f"Account Holder: {self.name}\n")
                file.write(f"Account Type: {self.accountType}\n")
                file.write(f"Initial Balance: {self.balance}\n")
                file.write("Transaction History:\n")
                file.write("-------------------------\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.record_transaction(f"Deposited: {amount}")
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.record_transaction(f"Withdrew: {amount}")
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def get_account_number(self):
        print(f"Account number: {self.accountNumber}")

    def get_user_name(self):
        print(f"Account holder: {self.name}")

    def get_account_type(self):
        print(f"Account type: {self.accountType}")

    def get_transaction_history(self):
        try:
            with open(self.filename, 'r') as file:
                print(file.read())
        except Exception as e:
            print(f"Error reading transaction history: {e}")

    def record_transaction(self, transaction):
        try:
            with open(self.filename, 'a') as file:
                file.write(f"{transaction}\n")
        except Exception as e:
            print(f"Error recording transaction: {e}")


def main():
    # Test cases
    account1 = BankAccount(name="John Doe", accountType="Savings")
    account2 = BankAccount(name="Jane Smith", accountType="Chequing")

    account1.deposit(500)
    account1.withdraw(200)
    account1.check_balance()
    account1.get_account_number()
    account1.get_user_name()
    account1.get_account_type()
    account1.get_transaction_history()

    account2.deposit(1000)
    account2.withdraw(300)
    account2.check_balance()
    account2.get_account_number()
    account2.get_user_name()
    account2.get_account_type()
    account2.get_transaction_history()


if __name__ == "__main__":
    main()
