def greeting(name="world"):
    print(f"Hello, {name}!")


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


class Person:
    def __init__(self, name):
        self.name = name