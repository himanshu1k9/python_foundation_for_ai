name = "Himanshu"
age = 31
salary = 55000
is_developer = True

price = 10.20

print(name, age, salary, is_developer, sep=" ")
print(type(name), type(age), type(salary), type(is_developer), type(price), sep=" ")

result = None
print(type(result))

# mutalbe lists
print(list(range(1, 8)))
print(list(range(-1, 8, -1)))

fruits = ["Orrange", "Papaya", "Banana"]
print(fruits)

features = [1500, 3, 2, 5]
print(features)
print(type(features))

# Tuples  ( Immutable )
house = (1500, 3, 2, 5)
print(type(house))

# Dictionary ( Key value pairs )
students = {
    "Himanshu": {
        "name": "Himanshu Vaidya",
        "age": 30,
        "is_developer": True
    },
    "Mohan": {
        "name": "Mohan",
        "age": 30,
        "is_developer": True
    }
}

print(students, type(students), sep=" ")

# Sets
numbers = {1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5}
print(numbers, type(numbers))

# Conditions
marks = 20
std = "10th"
result = None

if marks >= 90 and std == "10th":
    result = "A"
elif marks >= 80 and marks < 70 and std == "10th":
    result = "B"
elif marks >= 70 and marks < 60 and std == "10th":
    result = "C"
elif marks >= 60 and marks <= 50 and std == "10th":
    result = "D"
else:
    result = "F"

print(result)

# loops
for i in list(range(1, 8)):
    print(f"{i}th element is {i}", end=" ")

i = 1
while i <= 10:
    print("Himanshu")
    i += 1


# functions
def calculate_total(price, tax):
    return price + tax

print(calculate_total(200, 20))

# 2nd is the default argument
def pridict(area, bedrooms = 1):
    return f"aread should be {area} amd num of bedrooms should be {bedrooms}"

print(pridict(1500, 3)) # normal calls
print(pridict(bedrooms= 3, area= 1500)) # keyword arguments

# variable keyword arguments.
def configure_model(**settings):
    print(settings)

configure_model(temprature=0.7, max_tokens=500)

# Type hints
def add(x: float, y: float) -> float:
    return x + y

# x = float(input("Enter first number: "))
# y = float(input("Enter 2nd number: "))

# print(add(x, y))

# Exceptional handeling
try:
    20 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")