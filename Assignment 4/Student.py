class student:
    def __init__(self, rollno: int, name: str, course: str, marks: dict):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.marks = marks

    def __str__(self):
        return f"Roll no.: {self.rollno}\nName: {self.name}\nCourse: {self.course}\nMarks are: {self.marks}"

    @staticmethod
    def accept_studdata():
        rollno = int(input("Enter the roll number: "))
        name = input("Enter name of student: ")
        course = input("Enter course name: ")
        marks = {}
        subjects = ["Linux", "Java", "DBMS"]
        for s in subjects:
            mark = int(input(f"Enter marks of {s}: "))
            marks[s] = mark
        return Student(rollno, name, course, marks)

    def calculate_gpa(self):
        subjects = ["Linux", "Java", "DBMS"]
        weights = [1 / 3, 1 / 2, 1 / 4]
        gpa = 0
        for i in range(len(subjects)):
            gpa += weights[i] * self.marks[subjects[i]]
        return gpa


def display_all_students(students):
    if not students:
        print("No students in the list!")
        return
    print("\nAll Students:")
    for s in students:
        print(s)
        print(f"GPA: {s.calculate_gpa():.2f}\n")


def search_by_id(students, rollno):
    for s in students:
        if s.rollno == rollno:
            print(f"\nStudent found:\n{s}")
            print(f"GPA: {s.calculate_gpa():.2f}")
            return
    print(f"\nNo student found with roll number {rollno}")


def search_by_name(students, name):
    found = False
    for s in students:
        if s.name.lower() == name.lower():
            print(f"\nStudent found:\n{s}")
            print(f"GPA: {s.calculate_gpa():.2f}")
            found = True
    if not found:
        print(f"\nNo student found with name {name}")


def calculate_student_gpa(students, rollno):
    for s in students:
        if s.rollno == rollno:
            gpa = s.calculate_gpa()
            print(f"\nThe GPA of {s.name} is: {gpa:.2f}")
            return
    print(f"\nNo student found with roll number {rollno}")


def main():
    students = []
    s1 = student(1, "amar", "dbda", {"Linux": 45, "Java": 56, "DBMS": 32})
    s2 = student(2, "DJ", "dbda", {"Linux": 35, "Java": 86, "DBMS": 92})
    s3 = student(3, "ngsj", "dbda", {"Linux": 65, "Java": 38, "DBMS": 57})
    students.append(s1)
    students.append(s2)
    students.append(s3)

    while True:
        print("\n--- Student Management Menu ---")
        print("1. Display All Students")
        print("2. Search by ID")
        print("3. Search by Name")
        print("4. Calculate GPA of a Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case '1':
                display_all_students(students)
            case '2':
                rollno = int(input("Enter roll number to search: "))
                search_by_id(students, rollno)
            case '3':
                name = input("Enter name to search: ")
                search_by_name(students, name)
            case '4':
                rollno = int(input("Enter roll number to calculate GPA: "))
                calculate_student_gpa(students, rollno)
            case '5':
                print("Exiting program...")
                break
            case _:
                print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
