# PROBLEM 3 - PARAGRAPH SLICING
'''
Given the following paragraph: “About 40 Million Lightning Strikes Happen In The United States Each Year.
The Coldest Place On Earth Is At The East Antarctic Plateau In Antarctica. Clouds Are Not Made Of Gas.
Red Rain Can Happen. Fog Is Just A Low Cloud. Thundersnow: A Snowstorm With Thunder.”

- Use string slicing to print every 4th LETTER in the string starting from index 0 all the way to the end of the string.
 HINT: remember slicing has the syntax [start_index:stop_index:step]
'''

paragraph = "About 40 Million Lightning Strikes Happen In The United States Each Year. The Coldest Place on Earth Is At The Antartic Plateau In Antartica. Clouds Are Not Made Of Gas. Red Rain Can Happen. Fog Is Just A Low Cloud. Thundersnow: A Snowstorm With Thunder."
print(paragraph)

step = 4 # retrieve every xth Letter in a given string (does letter = character?)
start_index = step - 1
stop_index = len(paragraph)

output = paragraph[start_index:stop_index:step]
print(output)
print(paragraph[stop_index-4::-4]) # Prints every 4th character going in reverse
