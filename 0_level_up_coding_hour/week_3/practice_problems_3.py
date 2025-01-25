# PROBLEM 3
"""
You are given a list of temperatures…
		temps = [16.0, 28.7, 1.7, 4.7, 20.7, 16.3, 30.0, 27.0,
		23.1, 16.4, -3.5, 13.3, -4.0, 25.1, 27.2, 33.6, 1.1, 7.9,
		14.2, 18.4, 22.8, 29.4, -2.5, 21.5, 10.5, 25.6, -4.9, 24.5, 0.4, 17.3, -5.0]
Go through the list and print the value of a temperature only if it is above 18 degrees.
"""
temps = [16.0, 28.7, 1.7, 4.7, 20.7, 16.3, 30.0, 27.0,
		23.1, 16.4, -3.5, 13.3, -4.0, 25.1, 27.2, 33.6, 1.1, 7.9,
		14.2, 18.4, 22.8, 29.4, -2.5, 21.5, 10.5, 25.6, -4.9, 24.5, 0.4, 17.3, -5.0]

# Print the initial list of temperatures, sorted ascending
temp_threshold = 18
temps.sort()
print(temps)
temps_len = len(temps)
for i in range(temps_len):
    temp = temps[i]
    if temp > temp_threshold:
        print(temp)
    else:
        continue

