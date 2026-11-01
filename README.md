Collection Manipulator

Project Overview

Collection Manipulator is a menu-driven Python application developed to store and manage student information using different Python collection data types.

This project allows users to add new student records, display all student details, update student information, delete student records, and display unique subjects offered by students.

Features

1. Add Student

Collects student information such as name, age, grade, subjects, student ID, and date of birth.

Accepts multiple subjects separated by commas.

Stores student records in a list and dictionary.

Uses a tuple to store student ID and date of birth.

Uses a set to avoid duplicate subjects.

2. Display All Students

Displays all stored student records.

Shows student ID, name, age, grade, date of birth, and subjects.

Uses string formatting to display information clearly.

3. Update Student Information

Allows users to update existing student details using Student ID.

Updates name, age, grade, or subjects.

Maintains the student record in the dictionary and list.

4. Delete Student Record

Deletes a student record using Student ID.

Removes the record from both the list and dictionary.

Displays a confirmation message after deletion.

5. Display Subjects Offered

Displays all unique subjects offered by students.

Uses a set to avoid duplicate subjects.

Shows the subjects in alphabetical order.

6. Menu-Driven Interface

The program provides six menu options:

Add New Student.

Display All Students.

Update Student Information.

Delete Student Record.

Display Subjects Offered.

Exit the Program.

7. Error Handling and Input Validation

Checks for duplicate Student IDs.

Validates age and grade inputs.

Ensures required fields are not empty.

Displays appropriate error messages for invalid inputs.

Programming Concepts Used

Python Programming

List

Tuple

Set

Dictionary

for and while loops

if, elif, and else statements

break and continue statements

pass statement

del keyword

Type Casting (int() and float())

String Formatting (f-strings)

Mutability and Immutability

User Input and Input Validation

Technologies Used

Programming Language: Python 3

IDE: VS Code / Python IDLE

How to Run the Project

Clone or download this repository.

Open the project folder in VS Code or Python IDLE.

Open the terminal.

Run the following command:

python student_data_organizer.py

Sample Output

1. Main Menu

=============================================
WELCOME TO STUDENT DATA ORGANIZER
=============================================

This program allows you to manage student records.

========== MAIN MENU ==========
1. Add New Student
2. Display All Students
3. Update Student Information
4. Delete Student Record
5. Display Subjects Offered
6. Exit
===============================

Enter your choice (1-6):

2. Add Student

Enter your choice: 1

--- Add New Student ---

Enter Student ID: S101
Enter Student Name: Rahul
Enter Age: 20
Enter Grade: 85.5
Enter Date of Birth (DD-MM-YYYY): 15-05-2006
Enter Subjects (separated by commas): Python, Java, Maths

Student added successfully!

3. Display All Students

Enter your choice: 2

--- All Student Records ---

Student ID: S101
Name: Rahul
Age: 20
Grade: 85.50
Date of Birth: 15-05-2006
Subjects: Java, Maths, Python

-----------------------------------

4. Update Student Information

Enter your choice: 3

--- Update Student Information ---

Enter Student ID to update: S101

What would you like to update?
1. Name
2. Age
3. Grade
4. Subjects

Enter your choice: 1
Enter new name: Rahul Kumar

Student information updated successfully!

5. Delete Student Record

Enter your choice: 4

--- Delete Student Record ---

Enter Student ID to delete: S101

Student record deleted successfully!

6. Display Subjects Offered

Enter your choice: 5

--- Subjects Offered ---

- Java
- Maths
- Python

7. Exit Program

Enter your choice: 6

Thank you for using the Student Data Organizer!
Program exited successfully. Goodbye!
