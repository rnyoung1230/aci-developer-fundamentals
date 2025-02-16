# Banking System
import random
from datetime import date

class Currency:

    @staticmethod
    def format_currency(amount):
        return '${:,.2f}'.format(amount)

class Bank:
    name = "ABC Bank"
    active_accounts = []

    @staticmethod
    def assign_account_number():
        number = random.randint(1000001, 9999999)
        # If number already in use, find another
        while number in Bank.active_accounts:
            number = random.randint(1000001, 9999999)
        return number

    @staticmethod
    def open_account(account_type, opening_balance):
        account_num = Bank.assign_account_number()
        Bank.active_accounts.append(account_num)
        new_account = BankAccount(account_num, account_type, opening_balance)
        return new_account

    @staticmethod
    def close_account(account_num):
        Bank.active_accounts.pop(account_num)

class BankAccount:
    # class variables and methods
    minimum_balance = 100

    # instance variables and methods
    def __init__(self, account_num=None, account_type="Savings", opening_balance=minimum_balance):
        self.account_number = account_num
        self.account_type = account_type
        self.account_balance = opening_balance
        self.transaction_history = []

    def __str__(self):
        return f"BANK ACCOUNT SUMMARY\n" \
               f"Account Number: {self.account_number}\n" \
               f"Type: {self.account_type}\n" \
               f"Balance: {Currency.format_currency(self.account_balance)}\n" \
               f"Transaction History: {self.transaction_history}\n" \
               f"------------------------------------------"

    def make_deposit(self, amount):
        self.account_balance += amount
        new_transaction = BankTransaction("Deposit", amount)
        self.record_transaction(new_transaction)

    def make_withdrawal(self, amount):
        if self.account_balance - amount >= BankAccount.minimum_balance:
            self.account_balance -= amount
            new_transaction = BankTransaction("Withdrawal", amount)
            self.record_transaction(new_transaction)
        else:
            print(f"Insufficient funds. Withdrawal amount ({Currency.format_currency(amount)}) will cause your "
                  f"account balance ({Currency.format_currency(self.account_balance)}) "
                  f"to fall below the required minimum ({Currency.format_currency(BankAccount.minimum_balance)})")

    def record_transaction(self, transaction):
        transaction_record = {
            "transaction_id": transaction.transaction_id,
            "type": transaction.transaction_type,
            "amount": transaction.transaction_amount,
            "date": transaction.transaction_date
        }

        self.transaction_history.append(transaction_record)

class BankTransaction:
    # class variables and methods
    transaction_id = 1

    # instance variables and methods
    def __init__(self, transaction_type="Deposit", transaction_amount=None):
        BankTransaction.transaction_id += 1
        self.transaction_id = BankTransaction.transaction_id
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount

        today = date.today()
        formatted_date = today.strftime("%m-%d-%Y")
        self.transaction_date = formatted_date

    def __str__(self):
        return f"Id: {self.transaction_id}\n" \
               f"Type: {self.transaction_type}\n" \
               f"Amount: {Currency.format_currency(self.transaction_amount)}\n" \
               f"Date: {self.transaction_date}\n"

################################## TEST BANKING SYSTEM ##################################
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
accounts_set = set(Bank.active_accounts)
print(f"Set length: {len(accounts_set)}, List length: {len(Bank.active_accounts)}")
print(Bank.active_accounts)
print("----------------------------------------------------------------------")