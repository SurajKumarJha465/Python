# implention of dict variable
# it is use to store value in key-value pair

students = {"Hermiane":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin",
            }
print(students["Hermiane"])  # it will print Gryffindor
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#using loop

"""
for student in students:
    print(student)  #it will print only the keys

"""

# to print the key-value pair 
for student in students:
    print(student, students[student],sep = "->")

#list of Dictionary

Friends = [
    {"name": "Harry", "age": 20, "city": "London"},
    {"name": "Ron", "age": 21, "city": "London"},
    {"name": "Draco", "age": 22, "city": "London"},
    {"name": "Hermiane", "age": 23, "city": None},
]

#print(Friends[0]["name"])  # it will print Harry

for Friend in Friends:
    print(Friend["name"],Friend["age"],Friend["city"])

