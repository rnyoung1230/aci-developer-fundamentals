# Banking System
import random
from datetime import date

class CurrencyUtils:

    @staticmethod
    def format_currency(amount):
        return '${:,.2f}'.format(amount)

class DateUtils:

    @staticmethod
    def get_current_date():
        return date.today().strftime("%m-%d-%Y")

class Bank:
    name = "ABC Bank"
    accounts = []

    @staticmethod
    def assign_account_number():
        number = random.randint(1000000, 9999999)
        # If number already in use, find another
        while number in Bank.accounts:
            number = random.randint(1000000, 9999999)

        Bank.accounts.append(number)
        return number

class BankAccount:
    # class variables and methods
    minimum_balance = 100

    # instance variables and methods
    def __init__(self, account_num=None, account_type="Savings", opening_balance=minimum_balance, from_factory=False):
        if from_factory:
            self.account_number = account_num
            self.account_type = account_type
            self.account_status = "Active"
            self.account_balance = opening_balance
            self.transaction_history = []

            new_transaction = BankTransaction("Open Acct.", opening_balance)
            self.record_transaction(new_transaction)
        else:
            print("Cannot instantiate directly...use the BankAccount.open_account() method.")

    def __str__(self):
        transaction_history_display = ""
        for record in self.transaction_history:
            transaction_history_display += ' '.join(f'{k}: {str(v).ljust(12, " ")}'
                                                    for k, v in record.items()) + '\n'

        return f"\nBANK ACCOUNT SUMMARY\n" \
               f"Acct. Number: {self.account_number}\n" \
               f"Type: {self.account_type}\n" \
               f"Status: {self.account_status}\n" \
               f"Balance: {CurrencyUtils.format_currency(self.account_balance)}\n" \
               f"\nTRANSACTION HISTORY\n" \
               f"{transaction_history_display}\n" \
               f"------------------------------------------"

    @staticmethod
    def open_account(account_type, opening_balance=minimum_balance):
        account_num = Bank.assign_account_number()
        new_account = BankAccount(account_num, account_type, opening_balance, from_factory=True)
        return new_account

    def close_account(self):
        self.account_status = "Closed"
        self.make_withdrawal(self.account_balance)
        new_transaction = BankTransaction("Close Acct.")
        self.record_transaction(new_transaction)

    def make_deposit(self, amount):
        self.account_balance += amount
        new_transaction = BankTransaction("Deposit", amount)
        self.record_transaction(new_transaction)

    def make_withdrawal(self, amount):
        if self.account_balance - amount >= BankAccount.minimum_balance or self.account_status == "Closed":
            self.account_balance -= amount
            new_transaction = BankTransaction("Withdrawal", amount)
            self.record_transaction(new_transaction)
        else:
            print(f"Insufficient funds for account number {self.account_number}. Withdrawal amount ({CurrencyUtils.format_currency(amount)}) will cause your "
                  f"account balance ({CurrencyUtils.format_currency(self.account_balance)}) "
                  f"to fall below the required minimum ({CurrencyUtils.format_currency(BankAccount.minimum_balance)}).")

    def record_transaction(self, transaction):
        transaction_record = {
            "Type": transaction.transaction_type,
            "Date": transaction.transaction_date,
            "Amount": CurrencyUtils.format_currency(transaction.transaction_amount),
            "Updated Balance" : CurrencyUtils.format_currency(self.account_balance),
            "Transaction ID": transaction.transaction_id
        }

        self.transaction_history.append(transaction_record)

class BankTransaction:
    # class variables and methods
    transaction_id = 0

    # instance variables and methods
    def __init__(self, transaction_type="Deposit", transaction_amount=0):
        BankTransaction.transaction_id += 1
        self.transaction_id = BankTransaction.transaction_id
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = DateUtils.get_current_date()

    def __str__(self):
        return f"Transaction Id: {self.transaction_id} " \
               f"Date: {self.transaction_date} " \
               f"Amount: {CurrencyUtils.format_currency(self.transaction_amount)} " \
               f"Type: {self.transaction_type} "

            ################################## TEST BANKING SYSTEM ##################################
# Create a bunch of Checking and Savings accounts...execute deposit and withdrawal activities on each and then print a summary
bank_accounts = []
for i in range(10):
    new_checking_account = BankAccount.open_account(account_type="Checking", opening_balance=250)
    new_checking_account.make_deposit(random.randint(500, 1000))
    new_checking_account.make_withdrawal(random.randint(100, 1000))
    # Arbitrarily pick some accounts to test the close method on
    if new_checking_account.account_balance < 250:
        new_checking_account.close_account()
    bank_accounts.append(new_checking_account)
    #print(new_checking_account)

for i in range(10):
    new_savings_account = BankAccount.open_account(account_type="Savings")
    new_savings_account.make_deposit(random.randint(500, 1000))
    new_savings_account.make_withdrawal(random.randint(100, 1000))
    # Arbitrarily pick some accounts to test the close method on
    if new_savings_account.account_balance < 250:
        new_savings_account.close_account()
    bank_accounts.append(new_savings_account)
    #print(new_savings_account)

for account in bank_accounts:
    print(account)

# Confirm assign_account_number is working (no duplicates)...list and set lengths should match
accounts_set = set(Bank.accounts)
print(f"Set length: {len(accounts_set)}, List length: {len(Bank.accounts)}")
print("")
print(f"Bank Accounts:\n {Bank.accounts}")
print("----------------------------------------------------------------------")

# Confirm error message if user tries to directly instantiate a bank account
new_bank_account = BankAccount()