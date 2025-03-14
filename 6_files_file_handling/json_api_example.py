import requests, json

#API url
url = f"https://official-joke-api.appspot.com/random_joke"

#send the HTTP request
response = requests.get(url)

# figure out what we are working with
# print(type(response))
# get a list of attributes and methods we might be able to use
# print(dir(response))

# # view response
print(type(response.text))
print(response.text)


# the response.text is a <string> format, 
# convert from a json formatted string to a python dictionary
joke = json.loads(response.text)

# interact with dictionary
print(type(joke))

# for key, value in joke.items():
#     print(key, value)

print('---------')
print(joke['setup'])
input('press enter')
print(joke['punchline'])
