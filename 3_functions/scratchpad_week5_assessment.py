# Week 5 Assessment

# Question 1
cars = [
    {"car": "Volvo", "year": 2020},
    {"car": "Mitsubishi", "year": 2018},
    {"car": "BMW", "year": 2019},
    {"car": "Audi", "year": 2023}
]

def getYear(e):
    return e['year']

print(cars)
cars.sort(reverse=True, key=getYear)
#cars.sort(reverse=True, key=lambda a: a['year'])

print(cars)
print('-----------------------------------------')

# Question 2
def function1(user):
    newuser = user
    current_users.append(newuser)

newuser = 'Admin'
current_users = []

function1('Joy')
current_users.append(newuser)

print(current_users)