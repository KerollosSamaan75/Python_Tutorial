class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            print(student.display_info())
            print(f"Average Grade: {student.calculate_average()}")

def main():
    db = StudentDatabase()

    student1 = Student("Alice", 20, [85, 90, 78])
    student2 = Student("Bob", 22, [88, 92, 80])

    db.add_student(student1)
    db.add_student(student2)

    db.display_all_students()

main()
