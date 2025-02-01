import random

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, Grade: {self.grade})"

    def __lt__(self, other):
        return self.name < other.name  # Sorting based on name alphabetically

# Creating a list of students
students = [
    Student("Alice", 20, "A"),
    Student("Bob", 19, "B"),
    Student("Charlie", 21, "A"),
    Student("David", 22, "C"),
    Student("Eve", 20, "B"),
]

# Shuffle the student list
random.shuffle(students)
print("Shuffled List:")
for student in students:
    print(student)

# Sort the student list
students.sort()
print("\nSorted List:")
for student in students:
    print(student)

