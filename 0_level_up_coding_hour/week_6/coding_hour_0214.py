# CODING HOUR - 02/14

'''
xxxxxxxx
'''
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
        print(f"Bank Account Summary\n"
              f"Account Number: {self.account_number}\n"
              f"Type: {self.account_type}")

    def assign_account_number(self):
        return str(random.randrange(1000001, 9999999))

################################## TEST BANK ACCOUNT CREATION ##################################
for i in range(10):
    new_checking_account = BankAccount("Checking")

for i in range(10):
    new_savings_account = BankAccount()

print(created_accounts)
created_accounts_set = set(created_accounts)
print(len(created_accounts_set), len(created_accounts))