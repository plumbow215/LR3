"""
Author: Reymond John Vargas

"""

import random

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, Grade: {self.grade})"

    def __lt__(self, other):
        return self.name < other.name  

students = [
    Student("Alice", 20, "A"),
    Student("Bob", 19, "B"),
    Student("Ken", 21, "A"),
]

random.shuffle(students)
print("Shuffled List:")
for student in students:
    print(student)

students.sort()
print("\nSorted List:")
for student in students:
    print(student)

