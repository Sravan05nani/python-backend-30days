students = []


def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name should contain only letters.")
            continue

        return name


def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter marks (0 - 100): "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue

            return marks

        except ValueError:
            print("Invalid input. Enter a number.")


def student_exists(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


def add_student():
    name = get_valid_name()

    if student_exists(name):
        print("Student already exists.")
        return

    marks = get_valid_marks()

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students available.")
        return

    print("\n----- Student List -----")

    for i, student in enumerate(students, start=1):
        grade = get_grade(student["marks"])
        print(f"{i}. {student['name']} | Marks: {student['marks']} | Grade: {grade}")


def update_marks():
    if not students:
        print("No students available.")
        return

    name = get_valid_name()

    student = student_exists(name)

    if not student:
        print("Student not found.")
        return

    new_marks = get_valid_marks()
    student["marks"] = new_marks

    print("Marks updated successfully.")


def delete_student():
    if not students:
        print("No students available.")
        return

    name = get_valid_name()

    student = student_exists(name)

    if not student:
        print("Student not found.")
        return

    students.remove(student)
    print("Student removed successfully.")


def calculate_average():
    if not students:
        print("No students available.")
        return

    total = sum(student["marks"] for student in students)
    avg = total / len(students)

    print(f"Average marks: {avg:.2f}")


def show_topper():
    if not students:
        print("No students available.")
        return

    topper = max(students, key=lambda x: x["marks"])
    print(f"Topper: {topper['name']} with {topper['marks']} marks")


def sort_students():
    if not students:
        print("No students available.")
        return

    sorted_list = sorted(students, key=lambda x: x["marks"], reverse=True)

    print("\n----- Students Ranked -----")

    for i, student in enumerate(sorted_list, start=1):
        print(f"{i}. {student['name']} - {student['marks']}")


def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def statistics():
    if not students:
        print("No students available.")
        return

    marks = [s["marks"] for s in students]

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    print("\n----- Statistics -----")
    print(f"Total Students: {len(students)}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Average Marks: {average:.2f}")


def main():

    while True:

        print("\n========== Student Manager ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Average Marks")
        print("6. Show Topper")
        print("7. Sort Students")
        print("8. Statistics")
        print("9. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_marks()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            calculate_average()

        elif choice == "6":
            show_topper()

        elif choice == "7":
            sort_students()

        elif choice == "8":
            statistics()

        elif choice == "9":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()