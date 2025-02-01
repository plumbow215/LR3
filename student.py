"""
    Author: Roy Sedfrey
"""

class Student(object):

    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        return self.name
  
    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]
   
    def getAverage(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0
    
    def getHighScore(self):
        return max(self.scores) if self.scores else 0
 
    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        return self.getAverage() == other.getAverage()

    def __lt__(self, other):
        return self.getAverage() < other.getAverage()

    def __ge__(self, other):
        return self.getAverage() >= other.getAverage()

def main():
    student1 = Student("Ken", 5)
    student2 = Student("Alice", 5)
    student3 = Student("Bob", 5)

    student1.setScore(1, 90)
    student1.setScore(2, 80)
    student1.setScore(3, 85)
    student1.setScore(4, 95)
    student1.setScore(5, 100)

    student2.setScore(1, 70)
    student2.setScore(2, 75)
    student2.setScore(3, 80)
    student2.setScore(4, 85)
    student2.setScore(5, 90)

    student3.setScore(1, 90)
    student3.setScore(2, 90)
    student3.setScore(3, 90)
    student3.setScore(4, 90)
    student3.setScore(5, 90)

    print(student1)
    print(student2)
    print(student3)

    print(f"{student1.getName()} has the same average as {student3.getName()}: {student1 == student3}")
    print(f"{student1.getName()} has the same average as {student2.getName()}: {student1 == student2}")

    print(f"{student2.getName()} has a lower average than {student1.getName()}: {student2 < student1}")

    print(f"{student1.getName()} has a greater than or equal average to {student3.getName()}: {student1 >= student3}")
    print(f"{student2.getName()} has a greater than or equal average to {student1.getName()}: {student2 >= student1}")

if __name__ == "__main__":
    main()
