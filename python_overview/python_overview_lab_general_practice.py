# TASK 1A: GENERAL PYTHON PRACTICE
'''
The radius of a circle is 30 units. Use a variable called pi with a value of 3.14 to:

Calculate the area of a circle (pi*radius*radius) and assign the value to a variable name of area_of_circle, 
and print the radius of the circle using string formatting.

Take radius as user input and calculate the area, and print the radius of the circle using string formatting.
'''
radius = input("What is the radius you'd like to use?\n>")
radius = int(radius)
pi = 3.14
area_of_circle = pi * (radius * radius)
message1 = "The radius of the circle is {}."
print(message1.format(radius))
message2 = "The area of the circle is {}."
print(message2.format(area_of_circle))
print("")


# TASK 2B: GENERAL PYTHON PRACTICE
'''
Get user input for a temperature in Farenheit. Now convert this value to Celsius using the formula: C = (F − 32) × 5/9
'''
temperature_F = int(input("What is the temperature in Farenheit?\n>"))
temperature_C = (temperature_F - 32) * 5/9
print(f"The temperature in Farenheit is {temperature_F}.")
print(f"The temperature in Celsius is {temperature_C}.")
print("")


# TASK 3C: GENERAL PYTHON PRACTICE
'''
Given two variables with values x and y:

Get user input to assign different values to x and y.

Then swap the values so that y gets the original value of x and x gets the original value of y.

Hint: you may need a third variable to help with the swap. Try to draw a diagram as you contemplate how to solve this.
'''
x = input("Please enter a value.\n>")
print(f"Variable x has a value of \"{x}\".")
print("")
y = input("Please enter another value.\n>")
print(f"Variable y has a value of \"{y}\".")

print("Let's perform a swap...")
temp_varible = x
x = y
y = temp_varible
print(f"Variable x now has a value of \"{x}\".")
print(f"Variable y now has a value of \"{y}\".")
