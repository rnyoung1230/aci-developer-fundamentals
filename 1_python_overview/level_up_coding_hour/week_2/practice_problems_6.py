# PROBLEM 6
'''
Use a for loop and print statements to print this pattern:
  #
  ##
  ###
  ####
  #####
  ######
  #######
'''

# INITIALIZE PROGRAM
text_pattern = ""
number_of_times = 0
pattern_output = ""

# RUN PROGRAM
# Gather information from user
text_pattern = input("Please enter a character.\n>")
number_of_times = int(input("Please enter a number.\n>"))

# Take the entered information and output a text pattern that increments each line's representation by 1
# and uses the entered number as the number of lines to print
for number in range(0, number_of_times):
    pattern_output += text_pattern
    print(pattern_output)
        
# END PROGRAM
# Say good-bye
print("Good-bye!")

