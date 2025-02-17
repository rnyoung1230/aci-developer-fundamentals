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
        # Generate a candidate 8-digit number to use
        number = random.randint(10000000, 99999999)

        # Verify number isn't already assigned, keep generating numbers until you find one that's available
        while number in Bank.accounts:
            number = random.randint(10000000, 99999999)

        # Add the number to the list of assigned accounts
        Bank.accounts.append(number)
        return number

class BankAccount:
    # Class variables and methods
    minimum_balance = 100

    # Instance variables and methods
    def __init__(self, account_num=None, account_type=None, from_factory=False):
        if from_factory:
            self.account_number = account_num
            self.account_type = account_type
            self.account_status = "Active"
            self.account_balance = 0
            self.transaction_history = []
        else:
            print("Cannot instantiate directly...use the BankAccount.open_account() method.")

    def __str__(self):
        transaction_history_display = ""
        # Unpack the list of transaction events and format them into a line-by-line item display
        for record in self.transaction_history:
            transaction_history_display += ' '.join(f'{k}: {str(v).ljust(12, " ")}'
                                                    for k, v in record.items()) + '\n'

        # Format the BankAccount object and its transaction history into a print-friendly string
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
        # Find/Assign a unique number that identifies the account
        account_num = Bank.assign_account_number()

        # Create a BankAccount object
        new_account = BankAccount(account_num, account_type, from_factory=True)

        # Create a BankTransaction object to memorialize opening the account, log it to transaction history
        open_account_transaction = BankTransaction("Open Acct.")
        new_account.record_transaction(open_account_transaction)

        # Make an initial deposit to satisfy the min. balance requirement
        new_account.make_deposit(opening_balance)

        return new_account

    def close_account(self):
        # Update the account status
        self.account_status = "Closed"

        # Make a final withdrawal to zero out the account balance
        self.make_withdrawal(self.account_balance)

        # Create a BankTransaction object to memorialize closing the account, log it to transaction history
        close_account_transaction = BankTransaction("Close Acct.")
        self.record_transaction(close_account_transaction)

    def make_deposit(self, amount):
        # Update the account balance
        self.account_balance += amount

        # Create a BankTransaction object to memorialize the deposit, log it to transaction history
        deposit_transaction = BankTransaction("Deposit", amount)
        self.record_transaction(deposit_transaction)

    def make_withdrawal(self, amount):
        # Allow the withdrawal only if the account continues to meet the min. balance requirement OR
        # the account is closing
        if self.account_balance - amount >= BankAccount.minimum_balance or self.account_status == "Closed":

            # Update the account balance
            self.account_balance -= amount

            # Create a BankTransaction object to memorialize the withdrawal, log it to transaction history
            withdrawal_transaction = BankTransaction("Withdrawal", amount)
            self.record_transaction(withdrawal_transaction)
        else:
            # Provide a reason for denying the withdrawal request
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
    # Class variables and methods
    transaction_id = 0

    # Instance variables and methods
    def __init__(self, transaction_type=None, transaction_amount=0):
        BankTransaction.transaction_id += 1
        self.transaction_id = BankTransaction.transaction_id
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = DateUtils.get_current_date()

    def __str__(self):
        # Format the BankTransaction object into a print-friendly string
        return f"Transaction Id: {self.transaction_id} " \
               f"Date: {self.transaction_date} " \
               f"Amount: {CurrencyUtils.format_currency(self.transaction_amount)} " \
               f"Type: {self.transaction_type} "

            ################################## TEST BANKING SYSTEM ##################################
# Create a list to hold all the created accounts and their completed transactions
bank_accounts = []

for i in range(10):
    # Create a bunch of Checking accounts...execute deposit and withdrawal activities on each
    new_checking_account = BankAccount.open_account(account_type="Checking", opening_balance=250)
    new_checking_account.make_deposit(random.randint(500, 1000))
    new_checking_account.make_withdrawal(random.randint(100, 1000))

    # Arbitrarily pick some accounts to test the close method on
    if new_checking_account.account_balance < 250:
        new_checking_account.close_account()

    # Add each account to the bank_account list
    bank_accounts.append(new_checking_account)


for i in range(10):
    # Create a bunch of Savings accounts...execute deposit and withdrawal activities on each
    new_savings_account = BankAccount.open_account(account_type="Savings")
    new_savings_account.make_deposit(random.randint(500, 1000))
    new_savings_account.make_withdrawal(random.randint(100, 1000))

    # Arbitrarily pick some accounts to test the close method on
    if new_savings_account.account_balance < 250:
        new_savings_account.close_account()

    # Add each account to the bank_account list
    bank_accounts.append(new_savings_account)

# Print a summary for each account created above
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