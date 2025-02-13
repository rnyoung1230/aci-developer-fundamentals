# WEEK 6 - CLASSES AND OBJECTS

# Creating Classes and Objects
# class Employee:
#   status = "active"
#   hire_date = "01/01/2020"
#
#
# e1 = Employee()
# print(e1.hire_date)
#
# e1.hire_date = "02/23/2020"
# print(e1.hire_date)
# print("------------------------------------")
#
# # Challenge: Create a new employee
# e2 = Employee()
# e2.status = "Onboarding"
# e2.hire_date = "09/01/2023"
# print(e2.status)
# print(e2.hire_date)
# print("------------------------------------")
#
# # Creating Unique Objects with instance attributes
class Employee:
  employee_count = 0

  def __init__(self, name, email, hire_date):
    self.name = name
    self.email = email
    self.hire_date = hire_date
    Employee.employee_count += 1


e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")
print(e1.employee_count)
print(e1.name)
print(e1.email)
print(e1.hire_date)


e2 = Employee("Diego Ramirez", "diego.ramirez@example.com", "08/10/2022")
print(e2.employee_count)
print(e2.name)
print(e2.email)
print(e2.hire_date)

e3 = Employee("Robert Young", "ryoun3@gmail.com", "10/10/2024")
print(e3.employee_count)
print(e3.name)
print(e3.email)
print(e3.hire_date)

print("--------------------------")

# Creating instance methods
# class Employee:
#   employee_count = 0
#
#   def __init__(self, name, email, hire_date):
#     self.name = name
#     self.email = email
#     self.hire_date = hire_date
#     Employee.employee_count += 1
#
#     self.posts = []  # initiates list to hold user posts
#
#   def post(self, content):
#     new_post = content
#     self.posts.append(new_post)
#
#
# e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")
#
# e1.post("I learned a new skill!")
# e1.post("Ask me about learning Python")
# e1.post("Should I sign up for office hours?")
# e1.post("I'm having a great day!")
#
# print(e1.posts)
# print(e1.posts[2])

# Challenge: Defining a new class
class BankAccount():
  number_of_accounts = 0

  def __init__(self, balance):
    self.balance = balance

    BankAccount.number_of_accounts += 1
    account_number = BankAccount.number_of_accounts
    self.account_number = str(account_number)

  def deposit(self, amount):
    self.balance += amount

  def withdrawal(self, amount):
    if amount > self.balance:
      print("Insufficient funds.")
    else:
      self.balance -= amount

  def print_balance(self):
    print(f"The balance of account {self.account_number} is {self.balance}")

my_account = BankAccount(5000)
your_account = BankAccount(10)

my_account.print_balance()
my_account.withdrawal(1500)
my_account.print_balance()
print("--------------------------")
your_account.print_balance()
your_account.deposit(100)
your_account.print_balance()
your_account.withdrawal(150)

