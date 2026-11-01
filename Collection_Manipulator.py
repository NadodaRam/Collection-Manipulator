
# Student Data Organizer

# Collection Data Types
students = []          # List to store student records
student_data = {}      # Dictionary to organize records using Student ID


# Function to get non-empty input
def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


# Function to add a new student
def add_student():

    print("\n--- Add New Student ---")

    # Student ID validation
    while True:
        student_id = get_non_empty("Enter Student ID: ")

        if student_id not in student_data:
            break
        print("Student ID already exists! Enter a different ID.")

    name = get_non_empty("Enter Student Name: ")

    # Age type casting and validation
    while True:
        try:
            age = int(input("Enter Age: "))
            if age > 0:
                break
            print("Age must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")

    # Grade type casting
    while True:
        try:
            grade = float(input("Enter Grade: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    dob = get_non_empty("Enter Date of Birth (DD-MM-YYYY): ")

    # Store ID and DOB in an immutable tuple
    identity = (student_id, dob)

    # Store subjects in a set to avoid duplicates
    subjects = set()

    subject_input = get_non_empty(
        "Enter Subjects (separated by commas): "
    )

    for subject in subject_input.split(","):
        subject = subject.strip()
        if subject:
            subjects.add(subject)

    # Student information dictionary
    student = {
        "identity": identity,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    # Add student to list and dictionary
    students.append(student)
    student_data[student_id] = student

    print("\nStudent added successfully!")


# Function to display all students
def display_students():

    print("\n--- All Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:

        student_id, dob = student["identity"]

        print("\nStudent ID:", student_id)
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']:.2f}")
        print(f"Date of Birth: {dob}")
        print(f"Subjects: {', '.join(sorted(student['subjects']))}")

        print("-" * 35)


# Function to update student information
def update_student():

    print("\n--- Update Student Information ---")

    student_id = get_non_empty("Enter Student ID to update: ")

    if student_id not in student_data:
        print("Student ID not found!")
        return

    student = student_data[student_id]

    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Age")
    print("3. Grade")
    print("4. Subjects")

    choice = input("Enter your choice: ")

    if choice == "1":
        student["name"] = get_non_empty("Enter new name: ")

    elif choice == "2":
        while True:
            try:
                age = int(input("Enter new age: "))
                if age > 0:
                    student["age"] = age
                    break
                print("Age must be greater than zero.")
            except ValueError:
                print("Please enter a valid integer.")

    elif choice == "3":
        while True:
            try:
                student["grade"] = float(
                    input("Enter new grade: ")
                )
                break
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        new_subjects = get_non_empty(
            "Enter new subjects separated by commas: "
        )

        student["subjects"] = {
            subject.strip()
            for subject in new_subjects.split(",")
            if subject.strip()
        }

    else:
        print("Invalid choice!")
        return

    print("Student information updated successfully!")


# Function to delete a student
def delete_student():

    print("\n--- Delete Student Record ---")

    student_id = get_non_empty("Enter Student ID to delete: ")

    if student_id not in student_data:
        print("Student ID not found!")
        return

    # Find student in the main list
    for index, student in enumerate(students):

        if student["identity"][0] == student_id:

            # Delete record from the main list
            del students[index]

            # Delete record from the dictionary
            del student_data[student_id]

            print("Student record deleted successfully!")
            break


# Function to display unique subjects
def display_subjects():

    print("\n--- Subjects Offered ---")

    all_subjects = set()

    for student in students:
        all_subjects.update(student["subjects"])

    if all_subjects:
        for subject in sorted(all_subjects):
            print("-", subject)
    else:
        print("No subjects available.")


# Main Program
print("=" * 45)
print("WELCOME TO STUDENT DATA ORGANIZER")
print("=" * 45)

print("This program allows you to manage student records.")
print("You can add, display, update and delete students.")
print("You can also view all unique subjects offered.")

# Menu-driven interface
while True:

    print("\n========== MAIN MENU ==========")
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student Record")
    print("5. Display Subjects Offered")
    print("6. Exit")
    print("===============================")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_subjects()

    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        print("Program exited successfully. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 6.")
