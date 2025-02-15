import random

# created bank accounts
created_accounts = {"1000000": {
    "type": "Savings",
    "balance": 0
}
}

class BankAccount:
    # class variables and methods

    # instance variables and methods
    def __init__(self, account_type="Savings"):
        self.account_number = self.assign_account_number()
        while self.account_number in created_accounts:
            self.account_number = self.assign_account_number()

        self.account_type = account_type
        self.account_balance = 0

        created_accounts[self.account_number] = {"type": self.account_type, "balance": self.account_balance}

    def __str__(self):
        return f"BANK ACCOUNT SUMMARY\n"\
               f"Account Number: {self.account_number}\n"\
               f"Type: {self.account_type}\n"\
               f"Balance: {self.format_currency(self.account_balance)}\n"\
               f"------------------------------------------"

    def assign_account_number(self):
        return str(random.randint(1000001, 9999999))

    def make_deposit(self, amount):
        self.account_balance += amount

    def format_currency(self, amount):
        return '${:,.2f}'.format(amount)

################################## TEST BANK ACCOUNT CREATION ##################################
for i in range(5):
    new_checking_account = BankAccount("Checking")
    new_checking_account.make_deposit(random.randint(100, 1000))
    print(new_checking_account)

for i in range(5):
    new_savings_account = BankAccount()
    new_savings_account.make_deposit(random.randint(100, 1000))
    print(new_savings_account)

print(created_accounts)
created_accounts_set = set(created_accounts)
print(len(created_accounts_set), len(created_accounts))