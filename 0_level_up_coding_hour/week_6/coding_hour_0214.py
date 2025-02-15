# CODING HOUR - 02/14

'''
xxxxxxxx
'''
import random

class BankAccount:
    # unique accounts
    created_accounts = []

    # instance constructor
    def __init__(self):
        self.account_number = self.assign_account_number()
        while self.account_number in BankAccount.created_accounts:
            self.account_number = self.assign_account_number()

        BankAccount.created_accounts.append(self.account_number)
        self.account_balance = 0

    def assign_account_number(self):
        return random.randrange(1000000, 9999999)

################################## TEST BANK ACCOUNT CREATION ##################################
for i in range(50):
    my_account = BankAccount()
    print(my_account.account_number, my_account.account_balance)

print(BankAccount.created_accounts)
created_accounts_set = set(BankAccount.created_accounts)
print(len(created_accounts_set), len(BankAccount.created_accounts))