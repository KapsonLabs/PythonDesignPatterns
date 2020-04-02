"""
Author :  Allan Katongole
Date: 2nd April 2020
Role: Builder Design Pattern

Builder is a solution to antipattern called Telescoping Constructor
The telescoping constructor happens when an engineer attempts
to construct a complex object using an excessive number of constructors.

Partitions the buidlfing into 4 different roles
1. Director
2. Abstract Builder
3. Concrete Builder
4. Product
"""

class Director():

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    """Abstract Builder"""
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder --> Provides parts and tools to work on those parts"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self): 
        self.car.tires = "Tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"

class Car():
    """Product being built"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {} |'.format(self.model, self.tires, self.engine)


#Method and class invocations
builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)