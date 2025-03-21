# Banking System
import random
import utilities # custom utility methods (from utilities.py)

class BankAccount:
    # Class variables and methods
    reserved_account_numbers = []
    minimum_balance = 0
    annual_interest_rate = 0

    @classmethod
    def get_account_number(cls):
        # Generate a candidate 8-digit number to use
        number = random.randint(10000000, 99999999)

        # Verify number isn't already assigned, keep generating numbers until you find one that's available
        while number in cls.reserved_account_numbers:
            number = random.randint(10000000, 99999999)

        # Add the number to the list of assigned accounts
        cls.reserved_account_numbers.append(number)

        return number

    # Instance variables and methods
    def __init__(self, account_type=None, from_factory=False):
        # If this constructor was called from the open_account() factory method, assign values to the BankAccount object's attributes
        if from_factory:
            self.account_number = None
            self.account_type = account_type
            self.account_status = "Pending"
            self.account_balance = 0
            self.transaction_history = []
        else:
            # Inform the caller they cannot invoke the constructor directly...instead use static factory method
            print("Cannot instantiate directly...use the BankAccount.open_account() method.")

    def __str__(self):
        transaction_history_display = ""
        # Unpack the list of transaction events and format them into a line-by-line item display
        for record in self.transaction_history:
            transaction_history_display += ' '.join(f'{k}: {str(v).ljust(12, " ")}'
                                                    for k, v in record.items()) + '\n'
            # transaction_history_display += str(record) + '\n' --> for debugging

        # Format the BankAccount object and its transaction history into a print-friendly string
        return f"\nBANK ACCOUNT SUMMARY\n" \
               f"Acct. Number: {self.account_number}\n" \
               f"Type: {self.account_type}\n" \
               f"Interest Rate: {self.annual_interest_rate}%\n" \
               f"Status: {self.account_status}\n" \
               f"Balance: {utilities.format_currency(self.account_balance)}\n" \
               f"\nTRANSACTION HISTORY\n" \
               f"{transaction_history_display}\n" \
               f"------------------------------------------"

    @staticmethod
    def open_account(account_type=None, opening_balance=0):
        # Create a Savings or Checking account object
        if account_type == "Savings":
            new_account = SavingsAccount(account_type, from_factory=True)
        else:
            new_account = CheckingAccount(account_type, from_factory=True)

        if new_account.meets_min_balance_requirement(opening_balance):
            # Retrieve a number that uniquely identifies the account
            account_num = BankAccount.get_account_number()
            # Update the account with the new number and status from "Pending" to "Active"
            new_account.account_number = account_num
            new_account.account_status = "Active"

            # Create a BankTransaction object to memorialize opening the account, log it to transaction history
            open_account_transaction = BankTransaction("Open Acct.")
            new_account.record_transaction(open_account_transaction)

            # Make an initial deposit to satisfy the min. balance requirement
            new_account.make_deposit(opening_balance)

            return new_account

        else:
            print(f"You cannot open a {str(account_type).lower()} account with a balance "
                  f"less than {utilities.format_currency(new_account.minimum_balance)}.")

    def close_account(self):
        # Update the account status
        self.account_status = "Closed"

        # Make a final withdrawal to zero out the account balance
        self.make_withdrawal(self.account_balance)

        # Create a BankTransaction object to memorialize closing the account, log it to transaction history
        close_account_transaction = BankTransaction("Close Acct.")
        self.record_transaction(close_account_transaction)

    def make_deposit(self, deposit_amount):
        # Update the account balance
        self.account_balance += deposit_amount

        # Create a BankTransaction object to memorialize the deposit, log it to transaction history
        deposit_transaction = BankTransaction("Deposit", deposit_amount)
        self.record_transaction(deposit_transaction)

    def make_withdrawal(self, withdrawal_amount):
        # Allow the withdrawal as long as it doesn't result in an overdraft OR the account is closing
        if self.has_sufficient_funds(withdrawal_amount) or self.is_closed():

            # Update the account balance
            self.account_balance -= withdrawal_amount

            # Create a BankTransaction object to memorialize the withdrawal, log it to transaction history
            withdrawal_transaction = BankTransaction("Withdrawal", withdrawal_amount)
            self.record_transaction(withdrawal_transaction)

        else:

            print(f"Insufficient funds for {str(self.account_type).lower()} account number {self.account_number}. "
                   f"Withdrawal amount ({utilities.format_currency(withdrawal_amount)}) is greater than your current "
                  f"account balance ({utilities.format_currency(self.account_balance)}).")

    def pay_monthly_interest(self):
        if self.is_active() and self.meets_min_balance_requirement(self.account_balance):

            # Calculate the amount of interest to pay
            interest_amount = (self.account_balance * (self.annual_interest_rate/100)) / 12
            # Update the account balance
            self.account_balance += interest_amount
            # Create a BankTransaction object to memorialize the interest credit, log it to transaction history
            interest_credit_transaction = BankTransaction("Interest", interest_amount)
            self.record_transaction(interest_credit_transaction)

    def record_transaction(self, transaction):
        # Build a record to capture the event, along with the updated account balance
        # transaction_record = vars(transaction) # Returns the object as a dictionary (name-value pair)
        # transaction_record["balance"] = utilities.format_currency(self.account_balance)

        transaction_record = {
            "Date": transaction.date,
            "Type": transaction.type,
            "Amount": utilities.format_currency(transaction.amount),
            "Updated Balance" : utilities.format_currency(self.account_balance),
            "Transaction ID": transaction.id
        }

        # Append the event to the BankAccount object's transaction history
        self.transaction_history.append(transaction_record)

    def is_closed(self):
        return self.account_status == "Closed"

    def is_active(self):
        return self.account_status == "Active"

    def meets_min_balance_requirement(self, balance):
        return balance >= self.minimum_balance

    def is_overdrawn(self):
        return self.account_balance < 0

    def has_sufficient_funds(self, amount):
        return self.account_balance - amount >= 0

class SavingsAccount(BankAccount):
    # Class variables and methods
    minimum_balance = 100
    annual_interest_rate = 2.5

    # Instance variables and methods
    def __init__(self, account_type=None, from_factory=False):
        super().__init__(account_type, from_factory)

    def __str__(self):
        return super().__str__()

class CheckingAccount(BankAccount):
    # Class variables and methods
    minimum_balance = 250
    annual_interest_rate = 1.0

    # Instance variables and methods
    def __init__(self, account_type=None, from_factory=False):
        super().__init__(account_type, from_factory)

    def __str__(self):
        return super().__str__()

class BankTransaction:
    # Class variables and methods
    transaction_id = 0
    today = utilities.get_current_date()

    @classmethod
    def get_id(cls):
        # Increment the transaction id so this transaction has a unique identifier
        cls.transaction_id += 1
        return cls.transaction_id

    # Instance variables and methods
    def __init__(self, transaction_type=None, transaction_amount=0.0):
        # Assign values to the BankTransaction object's attributes
        self.id = BankTransaction.get_id()
        self.date = BankTransaction.today
        self.type = transaction_type
        self.amount = transaction_amount

    def __str__(self):
        # Format the BankTransaction object into a print-friendly string
        return f"Transaction Id: {self.id} " \
               f"Date: {self.date} " \
               f"Type: {self.type} " \
               f"Amount: {utilities.format_currency(self.amount)} "

            ################################## TEST BANKING SYSTEM ##################################
#Create a list to hold all the created accounts and their completed transactions
bank_accounts = []

for i in range(10):
    # Create a bunch of Checking accounts...execute deposit and withdrawal activities on each
    # Adjust the date between transaction types to make the history look more realistic/chronological in nature
    BankTransaction.today = utilities.adjust_date(BankTransaction.today, -10)
    new_checking_account = BankAccount.open_account(account_type="Checking", opening_balance=250)

    BankTransaction.today = utilities.adjust_date(BankTransaction.today, 5)
    new_checking_account.make_deposit(random.randint(500, 1000))

    BankTransaction.today = utilities.adjust_date(BankTransaction.today, 2)
    new_checking_account.make_withdrawal(random.randint(100, 1000))

    # Close any accounts that no longer meet the min. balance requirement
    if not new_checking_account.meets_min_balance_requirement(new_checking_account.account_balance):
        BankTransaction.today = utilities.get_current_date()
        new_checking_account.close_account()

    BankTransaction.today = utilities.adjust_date(BankTransaction.today, 15)
    new_checking_account.pay_monthly_interest()

    # Add each account to the bank_account list
    bank_accounts.append(new_checking_account)

for i in range(10):
    # Create a bunch of Savings accounts...execute deposit and withdrawal activities on each
    # Adjust the date between transaction types to make the history look more realistic/chronological in nature
    #new_savings_account = BankAccount.open_account(account_type="Savings")
    BankTransaction.today = utilities.adjust_date(BankTransaction.today, -10)
    new_savings_account = BankAccount.open_account("Savings", 100)

    BankTransaction.today = utilities.adjust_date(BankTransaction.today, 2)
    new_savings_account.make_deposit(random.randint(500, 1000))

    BankTransaction.today = utilities.adjust_date(BankTransaction.today, 6)
    new_savings_account.make_withdrawal(random.randint(100, 1000))

    # Close any accounts that no longer meet the min. balance requirement
    if not new_savings_account.meets_min_balance_requirement(new_savings_account.account_balance):
        BankTransaction.today = utilities.get_current_date()
        new_savings_account.close_account()

    BankTransaction.today = utilities.adjust_date(BankTransaction.today, 15)
    new_savings_account.pay_monthly_interest()

    # Add each account to the bank_account list
    bank_accounts.append(new_savings_account)

# Print a summary for each account created above
for account in bank_accounts:
    print(account)

# Confirm assign_account_number is working (no duplicates)...list and set lengths should match
account_numbers_set = set(BankAccount.reserved_account_numbers)
print(f"\nSet length: {len(account_numbers_set)}, List length: {len(BankAccount.reserved_account_numbers)}")
print("")
print(f"Bank Accounts:\n {BankAccount.reserved_account_numbers}")
print("----------------------------------------------------------------------")

# Confirm error message if user tries to directly instantiate a BankAccount object
print("\nTrying to directly instantiate a BankAccount object...")
bank_acct = BankAccount()
# Confirm error message if user tries to directly instantiate a SavingsAccount object
print("\nTrying to directly instantiate a SavingsAccount object...")
savings_acct = SavingsAccount()
# Confirm error message if user tries to directly instantiate a CheckingAccount object
print("\nTrying to directly instantiate a CheckingAccount object...")
checking_acct = CheckingAccount()
print("------------------------------------------------------------------------\n")

# Confirm SavingsAccount and CheckingAccount subclasses are working as expected
savings_account = BankAccount.open_account("Savings", 100)
print(type(savings_account))
print(savings_account)
print("")
checking_account = BankAccount.open_account("Checking", 250)
print(type(checking_account))
print(checking_account)
print("")

# Confirm SavingsAccount and CheckingAccount cannot be opened without meeting min. balance requirement
savings_account = BankAccount.open_account("Savings", 50)
checking_account = BankAccount.open_account("Checking", 150)
