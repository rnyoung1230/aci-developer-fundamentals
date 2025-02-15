import random

class Bank:

    name = "ABC Bank"

    accounts = {"1000000": {
        "type": "Savings",
        "balance": 0
    }
    }

    @staticmethod
    def open_account(account_type, opening_balance):
        new_account = BankAccount(account_type, opening_balance)
        Bank.accounts[new_account.account_number] = \
            {"type": new_account.account_type, "balance": new_account.account_balance}
        return new_account

    @staticmethod
    def close_account(account_num):
        Bank.accounts.pop(account_num)

    @staticmethod
    def assign_account_number():
        acct_num = random.randint(1000001, 9999999)
        # If account number already in use, find another
        while acct_num in Bank.accounts:
            acct_num = random.randint(1000001, 9999999)
        return acct_num

class BankAccount:
    # class variables and methods
    minimum_balance = 100

    @staticmethod
    def format_currency(amount):
        return '${:,.2f}'.format(amount)

    # instance variables and methods
    def __init__(self, account_type="Savings", opening_balance=minimum_balance):
        self.account_number = Bank.assign_account_number()
        self.account_type = account_type
        self.account_balance = opening_balance

    def __str__(self):
        return f"BANK ACCOUNT SUMMARY\n" \
               f"Account Number: {self.account_number}\n" \
               f"Type: {self.account_type}\n" \
               f"Balance: {BankAccount.format_currency(self.account_balance)}\n" \
               f"------------------------------------------"

    def make_deposit(self, amount):
        self.account_balance += amount
        Bank.accounts[self.account_number]["balance"] += amount

    def make_withdrawal(self, amount):
        if self.account_balance - amount >= BankAccount.minimum_balance:
            self.account_balance -= amount
            Bank.accounts[self.account_number]["balance"] -= amount
        else:
            print(f"Insufficient funds. Withdrawal amount ({BankAccount.format_currency(amount)}) will cause your "
                  f"account balance ({BankAccount.format_currency(self.account_balance)}) "
                  f"to fall below the required minimum ({BankAccount.format_currency(BankAccount.minimum_balance)})")


################################## TEST BANK ACCOUNT CREATION ##################################
for i in range(10):
    new_checking_account = Bank.open_account(account_type="Checking", opening_balance=250)
    new_checking_account.make_deposit(random.randint(500, 1000))
    new_checking_account.make_withdrawal(random.randint(100, 1000))
    print(new_checking_account)

for i in range(10):
    new_savings_account = Bank.open_account(account_type="Savings", opening_balance=100)
    new_savings_account.make_deposit(random.randint(500, 1000))
    new_savings_account.make_withdrawal(random.randint(100, 1000))
    print(new_savings_account)

# Confirm assign_account_number is working...list and set lengths should match
created_accounts_set = set(Bank.accounts)
print(f"Set length: {len(created_accounts_set)}, List length: {len(Bank.accounts)}")
print(Bank.accounts)
print("----------------------------------------------------------------------")

# Find any accounts where the balance is ABOVE $750 and close them
account_numbers = [x for x in Bank.accounts.keys() if Bank.accounts[x]["balance"] > 750] # list comprehension
for account_number in account_numbers:
    Bank.close_account(account_number)
    print(f"Account: {account_number} has been closed.")

# Print an updated list of accounts...should be less after account closures
print(Bank.accounts)
