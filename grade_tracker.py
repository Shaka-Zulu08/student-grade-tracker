import csv

def get_mark(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"
    

def save_students(students):
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for name, marks in students.items():
            writer.writerow([name] + marks)

def load_students():
    students = {}
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                marks = [int(mark) for mark in row[1:]]
                students[name] = marks
    except FileNotFoundError:
        pass
    return students

def delete_student(students):
    key_students = input("Enter the students to delete: ").capitalize()
    if key_students in students:
        del students[key_students]
        print(f"{key_students} has been deleted.")
    else:
        print(f"{key_students} not found in the records.")
    
    

students = load_students()

while True:
    print("\nWhat do you want to do? (Press 4 to save and quit)")
    print("1 - Add student")
    print("2 - Delete student")
    print("3 - View all students")
    print("4 - Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        while True:
            key_students = input("Enter student name: ").capitalize()
            if key_students in students:
                print("Student already exists.")
            elif key_students.lower() == "done":
                break
            else:   
                value_marks = [int(marks) for marks in input("Enter marks: ").split(",")]
                students[key_students] = value_marks

    elif choice == "2":
        delete_student(students)

    elif choice == "3":
        for names, marks in students.items():
            average = sum(marks) / len(marks)
            print(f"{names:10} : {average:.1f}% ~ {get_mark(average):3}")

    elif choice == "4":
        save_students(students)
        print("Students saved!")
        break