'''
1. Create a new Python file named "person.py". Define a class called "Person" with the following instance attributes:
    - name (string)
    - age (integer)
    - hobby(string)

Create the following methods:
    - A method called "introduce" that prints a greeting with the person's
      name and age.
    - A method called "have_birthday" that increments the person's age by 1.
    - A method called “what_hobby” that prints the name and hobby of the
      person.

Outside the class definition, create two Person objects and:
    - Call the "introduce" method for both objects.
    - Call the "have_birthday" method for one of the objects, then call
      "introduce" again to verify the age has increased.
    - Call the “what_hobby” method on the two-person objects.
'''

class Person:
    # class variables and methods

    # instance variables and methods

    def __init__(self, name=None, age=0, hobby=None):
        self.name = name
        self.age = age
        self.hobby = hobby

    def introduce(self):
        print(f"Hello {self.name}, it's nice to meet you! I heard you're {self.age} years old.")

    def have_birthday(self):
        self.age += 1

    def what_hobby(self):
        print(f"{self.name}'s favorite hobby is {self.hobby}.")


#################################  TEST PERSON CLASS  ##################################
person_1 = Person("Robert", 53, "playing pickleball")
person_2 = Person("Ben", 27, "fishing")

person_1.introduce()
person_2.introduce()
print("-----------------------------------------------")

person_1.have_birthday()
person_1.introduce()
print("-----------------------------------------------")

person_1.what_hobby()
person_2.what_hobby()