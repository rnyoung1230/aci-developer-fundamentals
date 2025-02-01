#create a dictionary for each friend with name, Responded, fav_food
friend_one = {'name':"Nicole", 'Response' : False, 'Fav_food':'cake'}
friend_two = {"name": "Nancy", 'Response' : False, "Fav_Food": "Pizza"}
friend_three = {"name": "John", 'Response' : False,  "Fav_Food": "Cupcake"}
friend_four = {"name": "Jane",'Response' : False,  "Fav_Food": "Pasta"}

#updating the fav_food value to be a list of foods

friend_one['Fav_food'] = ['cake', 'fried chicken', 'tacos']
friend_two["Fav_Food"] = ["Pizza", "Soda"]
friend_three["Fav_Food"] = ["Cupcake", "Icecream", "Pasta"]
friend_four["Fav_Food"] = ["Pasta", "Cupcake", "Lemonade"]

# friend_one['Invited'] = True
# print(friend_one)

#list of all the friends
list_friends = [friend_one, friend_two, friend_three, friend_four]
#print(list_friends[0])

'''
Create a main "birthday_party" dictionary that includes:
   - Basic party info: "host", "date", "time" and an "address"
   - An "activities" list with at least three planned activities - games, music, decorate your own cupcakes
   - A "menu" dictionary with keys for "main_course", "sides", "desserts", and "drinks", each containing a list of items
'''

birthday_party = {
    "host" : "Jane Doe",
    "date" : "Jan 31, 2025",
    "time" : "6 pm"
}

birthday_party['address'] = '123 Main St, Anytown, USA'
birthday_party['activities'] = ['games', 'music', 'decorate your own cupcakes']
birthday_party['menu'] = {'main_course':'value', 'sides': " ", "desserts" : " ", 'drinks': " "}

birthday_party['menu']['main_course'] = ['chicken', 'lasagna', 'burgers']
birthday_party['menu']['sides'] = ['Fries', "Salad", "Mashed Potatoes"]
birthday_party['menu']['desserts'] = ['cake', 'icecream']
birthday_party['menu']['drinks'] = ['lemonade', 'Soda']

#print(birthday_party)

#for each friend, print the party invite with all the details
for each_friend in list_friends:
    print(f"Dear {each_friend['name']}, You are invited to my birthday party on {birthday_party['date']} at {birthday_party['time']}.")
    print("\nHere is the menu for the party: ")
    
    for key in birthday_party['menu']:
        #print(key)
        print(f"{key}: {birthday_party['menu'][key]}")
    
    print("\nHere are the activities for the party: ")
    for activity in birthday_party['activities']:
        print(activity)
    

