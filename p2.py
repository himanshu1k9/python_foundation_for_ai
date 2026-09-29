import json

data = {
    "name": "Himanshu Vaidya",
    "age": 30,
    "department": "development",
    "is_active": True,
    # "getProfile": ():
    #     return this.name
    "skils": ["Frontend", "Backend", "Devops", "System design"]
}

json_data = json.dumps(data)
print(json_data, type(json_data))


# back
json_to_data = json.loads(json_data)
print(json_to_data, type(json_to_data))

# mutability
x = 10
x = 20
print(x)

# x = "abc"
# x[0] = "d"
# print(x) # throw error

# Mutables
list = [1,2,3,4,5]
list[0] = 100
print(list)

a = [1,2,3]
b = a
c = [1,2,3, 4]
b.append(4)
print(a)
print(b)

print(a == b)
print(a is b)
print(a == c, a is c)

b = a.copy()
b.append(20);

print(a, b, sep=" ")

students = [
    {
        "name": "Himabshu Vaidya",
        "age": 30
    },
    {
        "name": "Rahul Vaidya",
        "age": 30
    }
]

students_copy = students.copy()
print(students, students_copy)

students_copy[0] = {
    "name": "Muskan",
    "age": 26
}

print(students_copy, students)