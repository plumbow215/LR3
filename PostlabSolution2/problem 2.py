import random
from student import Student 

def main():
    students = [
        Student("Eve", 5),
        Student("Frank", 5),
        Student("Grace", 5),
        Student("Hank", 5),
        Student("Ivy", 5)
    ]
    
    for student in students:
        for i in range(1, 6):
            student.setScore(i, random.randint(60, 100))
    

    print("Initial Student Data:")
    for student in students:
        print(student, "\n")
    
    best_student = max(students, key=lambda s: s.getAverage())
    print(f"Top Student: {best_student.getName()} with an average score of {best_student.getAverage():.2f}")
    
    worst_student = min(students, key=lambda s: s.getAverage())
    print(f"Lowest Performing Student: {worst_student.getName()} with an average score of {worst_student.getAverage():.2f}")
    
if __name__ == "__main__":
    main()
