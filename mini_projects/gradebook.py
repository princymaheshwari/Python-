# This program implements a simple gradebook for a course.
# It allows the user to add students, add grade items,
# enter grades, and print student and class grades using
# an interactive text-based menu.

# Step 1: Writing the classes for custom errors

class EmptyRosterError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

class GradeItemNotFoundError(Exception):
    pass

# Step 2: Initialising a Student class that will act as the blueprint for student objects

class Student:

    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    # Getter methods
    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

# Step 3: Initialising a GradeItem class which will act as a blueprint for grade items

class GradeItem:

    def __init__(self, name_of_assignment, total_points_for_assignment):
        self.name_of_assignment = name_of_assignment
        self.total_points_for_assignment = total_points_for_assignment
        # Creating an empty dictionary for the grades in this assignment
        self.grades_for_assignment = {}

    # Writing methods to get name of the assignment and it's total points
    def get_name(self):
        return self.name_of_assignment

    def get_total_points(self):
        return self.total_points_for_assignment

    # Creating the add_student_grade method so that we can add the grade of a particular student
    def add_student_grade(self, student_id, grade):
        """Add or update a grade for a student for this grade item."""
        self.grades_for_assignment[student_id] = grade

    # Creating the get_student_grade() method which can tell the grade of a particular student in this assignment
    def get_student_grade(self, student_id):
        if student_id in self.grades_for_assignment:
            return self.grades_for_assignment[student_id]
        else:
            return None


# Step 4: Creating a Course class to keep track of and provide access to gradebook information

# Step 4: Course class

class Course:

    def __init__(self):
        self.roster = []        # list of Student objects
        self.grade_items = []   # list of GradeItem objects

    def add_student(self, student_object):
        self.roster.append(student_object)

    def add_grade_item(self, grade_item_object):
        self.grade_items.append(grade_item_object)

    def add_student_grade(self, grade_item_name, student_id, grade):
        # empty roster check
        if len(self.roster) == 0:
            raise EmptyRosterError("Exception: Course Roster is Empty.")

        # check if student exists
        student_exists = False
        for student in self.roster:
            if student.get_student_id() == student_id:
                student_exists = True
                break

        if not student_exists:
            raise StudentNotFoundError(
                "Exception: Student (" + str(student_id) + ") not found."
            )

        # find grade item
        grade_item_object = None
        for item in self.grade_items:
            if item.get_name() == grade_item_name:
                grade_item_object = item
                break

        if grade_item_object is None:
            raise GradeItemNotFoundError(
                "Exception: Grade Item (" + grade_item_name + ") not found."
            )

        # add the grade
        grade_item_object.add_student_grade(student_id, grade)

    def print_roster(self):
        if len(self.roster) == 0:
            raise EmptyRosterError("Exception: Course Roster is Empty.")

        print()
        print("Course Roster:")
        for student in self.roster:
            print(
                student.get_last_name() + ", " +
                student.get_first_name() + " (" +
                str(student.get_student_id()) + ")"
            )

    def print_student_grade(self, student_id):
        if len(self.roster) == 0:
            raise EmptyRosterError("Exception: Course Roster is Empty.")

        # find the student
        student_object = None
        for s in self.roster:
            if s.get_student_id() == student_id:
                student_object = s
                break

        if student_object is None:
            raise StudentNotFoundError(
                "Exception: Student (" + str(student_id) + ") not found."
            )

        # build single-line output: Last, First (ID) | HW1: 85 (100) | ...
        line = (
            student_object.get_last_name() + ", " +
            student_object.get_first_name() + " (" +
            str(student_object.get_student_id()) + ")"
        )

        for item in self.grade_items:
            grade = item.get_student_grade(student_id)
            if grade is None:
                grade_str = "N/A"
            else:
                grade_str = str(grade)
            line = (
                line + " | " + item.get_name() + ": " +
                grade_str + " (" + str(item.get_total_points()) + ")"
            )

        print()
        print(line)

    def print_class_grades(self):
        if len(self.roster) == 0:
            raise EmptyRosterError("Exception: Course Roster is Empty.")

        print()
        print("Class Grades:")

        for student in self.roster:
            line = (
                student.get_last_name() + ", " +
                student.get_first_name() + " (" +
                str(student.get_student_id()) + ")"
            )

            for item in self.grade_items:
                grade = item.get_student_grade(student.get_student_id())
                if grade is None:
                    grade_str = "N/A"
                else:
                    grade_str = str(grade)
                line = (
                    line + " | " + item.get_name() + ": " +
                    grade_str + " (" + str(item.get_total_points()) + ")"
                )

            print(line)


# Step 5: Menu / main program

def display_menu():
    print("Welcome to CSC/DSCI 1301: Principles in CS/DS 1")
    print("Please choose one of the following options (Enter 'quit' or 'q' to exit).")
    print("1) Add a Student.")
    print("2) Add a Grade Item.")
    print("3) Add a Student's Grade.")
    print("4) Print a Student's Grades.")
    print("5) Print Course Roster")
    print("6) Print Class Grades.")


def main():
    course = Course()
    print()
    display_menu()

    while True:
        
        print()
        choice = input()
        choice = choice.strip()

        if choice == "quit" or choice == "q":
            break

        elif choice == "1":
            # Add Student
            try:
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                student_id_str = input("Enter Student ID: ")
                student_id = int(student_id_str)

                student = Student(student_id, first_name, last_name)
                course.add_student(student)
            except ValueError:
                print("Error: Enter a Integer Student ID")

        elif choice == "2":
            # Add Grade Item
            name = input("Enter grade item name: ")
            total_points_str = input("Enter the total points for the grade item: ")
            try:
                total_points = float(total_points_str)
                grade_item = GradeItem(name, total_points)
                course.add_grade_item(grade_item)
            except ValueError:
                print("Error: Enter a numeric value for total points.")

        elif choice == "3":
            # Add Student Grade
            grade_item_name = input("Enter grade item name: ")
            student_id_str = input("Enter Student ID: ")
            print()
            grade_str = input("Enter Student Grade: ")

            try:
                student_id = int(student_id_str)
                grade = float(grade_str)

                try:
                    course.add_student_grade(grade_item_name, student_id, grade)
                except EmptyRosterError:
                    print("Error: Course Roster is Empty!")
                except StudentNotFoundError:
                    print("Error: Student (" + student_id_str + ") not found.")
                except GradeItemNotFoundError:
                    print("Error: Grade Item (" + grade_item_name + ") not found.")

            except ValueError:
                # you can change this message if your instructor wants
                print("Error: Enter a Integer Student ID")

        elif choice == "4":
            # Print a Student's Grades
            student_id_str = input("Enter Student ID: ")

            try:
                student_id = int(student_id_str)

                try:
                    course.print_student_grade(student_id)
                except EmptyRosterError:
                    print("Error: Course Roster is Empty!")
                except StudentNotFoundError:
                    print("Error: Student (" + student_id_str + ") not found.")

            except ValueError:
                print("Error: Enter a Integer Student ID")

        elif choice == "5":
            # Print Course Roster
            try:
                course.print_roster()
            except EmptyRosterError:
                print("Error: Course Roster is Empty!")

        elif choice == "6":
            # Print Class Grades
            try:
                course.print_class_grades()
            except EmptyRosterError:
                print("Error: Course Roster is Empty!")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
