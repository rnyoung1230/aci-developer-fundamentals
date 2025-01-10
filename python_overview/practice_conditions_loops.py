# Using conditionals with proper indentation
x = 5

if x > 5:  
    print(f"{x} is greater than 5")  # Indented: Belongs to the if block
elif x == 5:
    print(f"{x} is equal to 5")  # Indented: Belongs to the elif block
else:
    print(f"{x} is less than 5")  # Indented: Belongs to the else block

print("Condition check complete!")  # Not indented: Runs after the if-elif-else block

x = 11
y = 200

if y > x:
    print(f"{y} is greater than {x}")

print("This is outside the if statement and will always print.")

a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")
    print("Next action")
    
x = 200
y = 200

if y > x:
  print("y is greater than x")
elif y == x:
  print("y and x are equal")
  
x = 300
y = 200

if y > x:
    print('y is greater than x')
elif y == x:
    print('y and x are equal')
else:
    print('x is greater than y')
    
# Loops with ranges
# Using a for loop to print numbers from 1 to 100
for number in range(1, 101):  # Start at 1, end at 100
    print(number)  # Indented: This is part of the loop
    print("This line also runs inside the loop.")  # Also part of the loop

# Code at this level will not be part of the loop
print("Loop is complete!")

# A string to loop through
message = "Hello"

#Loop through each character in the string
for character in message:
    print(character) # This prints each character from string on a new line
    
# Iterating over a loop
numbers = [1, 2, 3, 4, 5]

for number in numbers: 
  print(number)

# While loops
count = 1
while count <= 5:
    print(count)
    count += 1
    
play_again = 'Y'

while (play_again == 'Y'):
    play_again = input('Would you like to play again (Y/N)? ')

print('Thanks for playing! Goodbye.')

# Break statements
word = 'apple'

for letter in word: 
    if letter == 'l':
        print(f"We found the letter \"{letter}\".")
        break
    print(letter)
    
    