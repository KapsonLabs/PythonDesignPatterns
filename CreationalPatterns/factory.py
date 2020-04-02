"""
Author :  Allan Katongole
Date: 2nd April 2020
Role: Factory Design Pattern
"""

class Dog:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "woof"


class Cat:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "meow"


def get_pet(pet="dog"):
    """The factory method"""

    pets = dict(dog=Dog("Hanny"), cat=Cat("Panny"))
    return pets[pet]

#Class invocation
d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())