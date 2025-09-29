"""Q 1. Create a class 'Student' with rollno, studentName, course ,dictionary of
marks(subjectName -> marks [5]). Provide following functionalities
A. initializer
B. override __str__ method
C. accept student data
D. Print student data for given id.
E. Print Student who has failed in any subject. """


class Student:
    def __init__(self, rollno: int, name: str, course: str, marks: dir()):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.marks = marks

    def __str__(self):
        return f"Roll no.: {self.rollno}\nName: {self.name}\ncourse: {self.course}\nmarks are: {self.marks}"

    @staticmethod
    def accept_studdata():
        rollno = int(input("Enter the roll number: "))
        name = input("Enter name of student: ")
        course = input("Enter course name: ")
        marks = {}
        subjects = ["Linux", "Java", "DBMS", "Python", "ML"]
        for s in subjects:
            mark = int(input(f"Enter marks of {s}: "))
            marks[s] = mark
        return Student(rollno, name, course, marks)

    @staticmethod
    def display_studdata(students, rollno):
        for i in students:
            if i.rollno == rollno:
                print(f"The student at {rollno} is: {i}")
            else:
                print(f"The student for roll no {rollno} does not exist!")

    @staticmethod
    def display_studdata1(students, name1):
        for i in students:
            if i.name == name1:
                print(f"The student at {name1} is: {i}")
            else:
                print(f"The student for roll no {name1} does not exist!")

    @staticmethod
    def failed_student(students):
        print("Student who failed in at least one subject is:")
        found = False
        for i in students:
            if any(mark < 40 for mark in i.marks.values()):
                print(i)
                found = True
        if not found:
            print("No student has failed in any subject")


if __name__ == "__main__":

    students = []
    # n = int(input("Enter total no of students: "))

    for i in range(5):
        print(f"Enter details for student {i + 1}:")
        student = Student.accept_studdata()
        students.append(student)

    roll_to_find = int(input("Enter the roll no of student u want to find:"))
    Student.display_studdata(students, roll_to_find)

    Student.failed_student(students)
    name1 = input("Enter the name of student u want to find:")
    Student.display_studdata1(students, name1)
