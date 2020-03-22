# Student: Elmer Camargo

# Python app connecting to sqlite db using both pandas and the sqlite

import pandas as pd
import sqlite3

from src.Student import Student


def get_int(prompt, lower, upper):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print('Please enter numeric values only')
            continue
        if value < lower or value > upper:
            print("Your input must be within given range")
            continue
        else:
            break
    return value


def get_string(prompt):
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print('Please enter character values only')
            continue
        if len(value) == 0:
            print("Your input must contain characters")
            continue
        else:
            break
    return value


print('Connecting to database')

# Database connection

try:
    db = sqlite3.connect('data/Students.sqlite')
    c = db.cursor()
    table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", db)
    print('Available tables: ', table.head())
except:
    print('Error: try making sure db is in data folder')
    exit()
else:
    print('Successful Connection')

flag = True

while flag:

    user_input = get_int('\nPlease choose action desired\n\n'
                         '1 - Display all students\n'
                         '2 - Insert a student\n'
                         '3 - Update student by student id\n'
                         '4 - Delete student by student id\n'
                         '5 - Search students by major, gpa, or advisor\n'
                         '0 - Exit\n\n'
                         'Please enter corresponding number: ', 0, 5)

    if user_input == 1:

        query = "SELECT * FROM Student WHERE isDeleted = 0"
        df = pd.read_sql_query(query, db)

        print(df)

        input("Press Enter to continue...")

    # Create student and add to db
    elif user_input == 2:

        first = get_string("Please input student first name: ")
        last = get_string("Please input student last name: ")
        gpa = get_int('Please input student GPA: ', 0, 4)
        major = get_string("Please input student major: ")
        faculty_advisor = get_string("Please input student faculty_advisor: ")

        stu = Student(first, last, gpa, major, faculty_advisor)

        c.execute("INSERT INTO Student(FirstName, LastName, GPA, Major, FacultyAdvisor, isDeleted)"
                  "VALUES (?,?,?,?,?,?)", stu.getStudent())

        db.commit()

        studentID = c.lastrowid
        print('Last ID is: ', studentID)

    elif user_input == 3:

        search = get_int("\nPlease select field you would like to update\n\n"
                         "1 - Change major\n"
                         "2 - Update advisor\n"
                         "0 - Main Menu\n\n"
                         "Please enter corresponding number: ", 0, 2)

        if search == 1:
            student_id = get_int("Please enter StudentID of student you would like to update: ", 0, 10000)
            major = get_string("Please enter new student major: ")
            major = major.lower()
            update = (major, student_id,)

            c.execute('UPDATE Student SET Major = ? WHERE StudentId = ?', update)
            db.commit()

        elif search == 2:
            student_id = get_int("Please enter StudentID of student you would like to update: ", 0, 10000)
            advisor = get_string("Please enter new student advisor: ")
            advisor = advisor.lower()
            update = (advisor, student_id,)

            c.execute('UPDATE Student SET FacultyAdvisor = ? WHERE StudentId = ?', update)
            db.commit()

        elif search == 0:
            print('Returning to menu')
            continue

    elif user_input == 4:
        student_id = get_int("Please enter StudentID of student you would like to delete: ", 0, 10000)
        student_id = (student_id,)

        c.execute('UPDATE Student SET isDeleted = 1 WHERE StudentId = ?', student_id)
        db.commit()
        print('Student deleted\n')

    elif user_input == 5:
        search = get_int("\nPlease select search criteria\n\n"
                         "1 - Search by major\n"
                         "2 - Search by GPA\n"
                         "3 - Search by advisor\n"
                         "0 - Main Menu\n\n"
                         "Please enter corresponding number: ", 0, 3)

        if search == 1:
            major = get_string("Please enter major name: ")
            major = (major.lower(), 0,)

            c.execute('SELECT * FROM Student WHERE Major = ? AND isDeleted = ?', major)

            all_rows = c.fetchall()
            print(pd.DataFrame(all_rows))

            input("Press Enter to continue...")

        elif search == 2:
            gpa = get_int("Please enter gpa: ", 0, 4)
            gpa = (gpa, 0,)

            c.execute('SELECT * FROM Student WHERE GPA = ? AND isDeleted = ?', gpa)

            all_rows = c.fetchall()
            print(pd.DataFrame(all_rows))

            input("Press Enter to continue...")

        elif search == 3:
            advisor = get_string("Please enter advisor name: ")
            advisor = (advisor, 0,)

            c.execute('SELECT * FROM Student WHERE FacultyAdvisor = ? AND isDeleted = ?', advisor)

            all_rows = c.fetchall()
            print(pd.DataFrame(all_rows))

            input("Press Enter to continue...")

        elif search == 0:
            print("Returning to main menu.")

    elif user_input == 0:
        print('0 was pressed now exiting')
        flag = False

    else:
        print('Please only enter numbers 0-5')

print('Application Closing')