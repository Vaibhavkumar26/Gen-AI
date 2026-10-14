
import json


class Bank_Account:
    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = str(account_no)
        self.balance = balance
        self.transaction_history = []

    def deposit_money(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero")
        else:
            self.balance += amount

            self.transaction_history.append({
                "type": "Deposit",
                "amount": amount,
                "balance": self.balance
            })

            print("Money deposited successfully")

    def withdraw_money(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

            self.transaction_history.append({
                "type": "Withdrawal",
                "amount": amount,
                "balance": self.balance
            })

            print("Money withdrawn successfully")

    def check_balance(self):
        print("Account holder:", self.name)
        print("Account number:", self.account_no)
        print("Current balance:", round(self.balance, 2))

    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions found")
            return

        for transaction in self.transaction_history:
            print(
                transaction["type"],
                "| Amount:", transaction["amount"],
                "| Balance:", transaction["balance"]
            )


class Bank_Management:
    def __init__(self):
        self.account_list = {}
        self.load_data()

    def create_account(self, name, account_no):
        account_no = str(account_no)

        if account_no in self.account_list:
            print("Account already exists")
        else:
            account = Bank_Account(name, account_no)
            self.account_list[account_no] = account
            print("Account created successfully")

    def deposit_money(self, account_no, amount):
        account = self.account_list.get(str(account_no))

        if account:
            account.deposit_money(amount)
        else:
            print("Account not found")

    def withdraw_money(self, account_no, amount):
        account = self.account_list.get(str(account_no))

        if account:
            account.withdraw_money(amount)
        else:
            print("Account not found")

    def check_balance(self, account_no):
        account = self.account_list.get(str(account_no))

        if account:
            account.check_balance()
        else:
            print("Account not found")

    def show_transaction_history(self, account_no):
        account = self.account_list.get(str(account_no))

        if account:
            account.show_transaction_history()
        else:
            print("Account not found")

    def display_accounts(self):
        if not self.account_list:
            print("No accounts found")
            return

        for account in self.account_list.values():
            account.check_balance()
            print()

    def save_data(self):
        records = []

        for account in self.account_list.values():
            records.append({
                "name": account.name,
                "account_no": account.account_no,
                "balance": account.balance,
                "transaction_history": account.transaction_history
            })

        with open("bank_records.json", "w") as file:
            json.dump(records, file, indent=4)

        print("Data saved successfully")

    def load_data(self):
        try:
            with open("bank_records.json", "r") as file:
                records = json.load(file)

            for record in records:
                account = Bank_Account(
                    record["name"],
                    record["account_no"],
                    record["balance"]
                )

                account.transaction_history = record.get(
                    "transaction_history", []
                )

                self.account_list[account.account_no] = account

        except FileNotFoundError:
            pass


def main():
    bank = Bank_Management()

    while True:
        print("\n----- BANK ACCOUNT MANAGEMENT SYSTEM -----")
        print("1. Create account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Show transaction history")
        print("6. Display all accounts")
        print("7. Save data")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            account_no = input("Enter account number: ")

            bank.create_account(name, account_no)

        elif choice == "2":
            account_no = input("Enter account number: ")

            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit_money(account_no, amount)
            except ValueError:
                print("Please enter a valid amount")

        elif choice == "3":
            account_no = input("Enter account number: ")

            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw_money(account_no, amount)
            except ValueError:
                print("Please enter a valid amount")

        elif choice == "4":
            account_no = input("Enter account number: ")
            bank.check_balance(account_no)

        elif choice == "5":
            account_no = input("Enter account number: ")
            bank.show_transaction_history(account_no)

        elif choice == "6":
            bank.display_accounts()

        elif choice == "7":
            bank.save_data()

        elif choice == "0":
            bank.save_data()
            print("Exiting bank management system")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
