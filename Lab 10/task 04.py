def add_student(student_list, name):
    student_list.append(name)
    print(f"{name} has been added.")

def remove_student(student_list, name):
    if name in student_list:
        student_list.remove(name)
        print(f"{name} has been removed.")
    else:
        print(f"{name} not found.")

def list_students(student_list):
    print("Current students:")
    for student in student_list:
        print("-", student)

# Example usage
students = ["Alice", "Bob", "Charlie"]

def welcome_students(student_list):
    print("Welcome students:")
    for student in student_list:
        print("-", student)

welcome_students(students)
add_student(students, "David")
remove_student(students, "Bob")
list_students(students)
