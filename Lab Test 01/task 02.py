class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display_details(self):
        if 90 <= self.marks <= 100:
            grade = "A+"
        elif 75 <= self.marks < 90:
            grade = "A"
        elif 60 <= self.marks < 75:
            grade = "B"
        elif 50 <= self.marks < 60:
            grade = "C"
        else:
            grade = "F (Fail)"
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.rollno}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {grade}")

if __name__ == "__main__":
    name = input("Enter student's name: ")
    rollno = input("Enter student's roll number: ")
    try:
        marks = float(input("Enter student's marks: "))
        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
        else:
            student = Student(name, rollno, marks)
            student.display_details()
    except ValueError:
        print("Invalid input for marks. Please enter a number.")
