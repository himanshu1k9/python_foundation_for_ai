class House:
    # pass
    # Attributes through constructor
    def __init__(self, area, bedrooms):
        self.area = area
        self.bedrooms = bedrooms

    # Method
    def describe(self):
        return f"Area is {self.area} and bedrooms are {self.bedrooms}"

    # Static method
    # @staticmethod
    # def add(a, b):
    #     return a + b

house = House(1500, 3)
print(type(house))
print(house.area, house.bedrooms, sep=" ")
print(house.describe())
# print(House.add(10, 20)) # Calling static method

# Example of static method in python
class Test:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def print_sum(cls, a, b):
        return a + b

    def test_method(self, a, b):
        return Test.print_sum(a, b)

print(Test.add(10,20))

test = Test()
print(test.test_method(100, 200))

# Example of compositions
class Database:
    pass

class AiService:
    def __init__(self, database):
        self.database = database

database = Database()
ai_service = AiService(database)

print(ai_service)

# Inheritence in python
class A:
    pass

class B(A):
    pass

# Abstract classes
from abc import abstractmethod

# class LLMProvider(ABC):
#     @abstractmethod
#     def generate(self, promt: str) -> str:
#         pass


# class Provider(LLMProvider):
#     def generate(self, promt: str) -> str:
#         return '.....'

# Powefull package for data mapping
from dataclasses import dataclass

@dataclass
class House:
    area: int
    bedrooms: int
    bathrooms: int
    age: int

house = House(area=1500, bedrooms= 3, bathrooms= 4, age= 10)
print(house)

# Properties
class Model:
    def __init__(self, temprature):
        self._temprature = temprature

    @property
    def temprature(self):
        return self._temprature

model1 = Model(0.7)
print(model1._temprature) # this also works
# print(model1.temprature()) # Giving error since its look like method but it's property
print(model1.temprature)