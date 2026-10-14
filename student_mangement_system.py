import json


subject_branches = {
    "ee": [
        "power_system", "electrical_networks", "semiconductors", "maths"
    ],
    "cs": [
        "DSA", "probability", "DBMS", "Networking", "System Design"
    ],
    "ce": [
        "fluid mechanics", "mechanical_strength", "earthquakes", "torsion"
    ]
}


class Student:

    def __init__(self, name, roll_no, class_division, branch):
        self.name = name
        self.roll_no = str(roll_no)
        self.class_division = class_division
        self.branch = branch
        self.marks = {}


class School_Attendence:
    
    def __init__(self):
        self.student_list = {}
        self.load_records()

    def enrolling_student(self, student):
        if student.roll_no in self.student_list:
            print("Student already exists")
        else:
            self.student_list[student.roll_no] = student
            print("Student added successfully")

    def display_students(self):
        if not self.student_list:
            print("No students found")
            return

        for student in self.student_list.values():
            print(
                student.name,
                student.roll_no,
                student.class_division,
                student.branch
            )

    def search_student(self, roll_no):
        student = self.student_list.get(str(roll_no))

        if student:
            print("Name:", student.name)
            print("Roll number:", student.roll_no)
            print("Class division:", student.class_division)
            print("Branch:", student.branch)
            print("Marks:", student.marks)
        else:
            print("Student not found")

    def updating_student_accord(self, roll_no, student):
        if roll_no in self.student_list:
            student.marks = self.student_list[roll_no].marks
            self.student_list[roll_no] = student
            print("Student record updated")
        else:
            print("Student not found")

    def deleting_student(self, roll_no):
        if roll_no in self.student_list:
            del self.student_list[roll_no]
            print("Student deleted")
        else:
            print("Student not found")

    def average_marks(self, roll_no):
        if roll_no not in self.student_list:
            print("Student not found")
            return

        student = self.student_list[roll_no]
        subjects = subject_branches[student.branch]

        if not student.marks:
            marks = {}

            for subject in subjects:
                mark = int(input(f"Enter marks for {subject}: "))

                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100")
                    return

                marks[subject] = mark

            student.marks = marks

        total = sum(student.marks.values())
        average = total / len(student.marks)

        print("Total marks:", total)
        print("Average marks:", average)

    def save_records(self):
        records = []

        for student in self.student_list.values():
            records.append({
                "name": student.name,
                "roll_no": student.roll_no,
                "class_division": student.class_division,
                "branch": student.branch,
                "marks": student.marks
            })

        with open("student_records.json", "w") as file:
            json.dump(records, file, indent=4)

        print("Records saved successfully")

    def load_records(self):
        try:
            with open("student_records.json", "r") as file:
                records = json.load(file)

            for record in records:
                student = Student(
                    record["name"],
                    record["roll_no"],
                    record["class_division"],
                    record["branch"]
                )

                student.marks = record.get("marks", {})
                self.student_list[student.roll_no] = student

        except FileNotFoundError:
            pass


def main():
    school = School_Attendence()

    while True:
        print("\n----- STUDENT MANAGEMENT SYSTEM -----")
        print("1. Add students")
        print("2. Display students")
        print("3. Search students")
        print("4. Update student records")
        print("5. Delete students")
        print("6. Calculate average marks")
        print("7. Save records")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll_no = input("Enter roll number: ")
            division = input("Enter class division: ")
            branch = input("Enter branch:  , (CE/CS/EE) ").lower().strip()

            if branch not in subject_branches:
                print("Invalid branch")
                continue

            student = Student(name, roll_no, division, branch)
            school.enrolling_student(student)

        elif choice == "2":
            school.display_students()

        elif choice == "3":
            roll_no = input("Enter roll number: ")
            school.search_student(roll_no)

        elif choice == "4":
            roll_no = input("Enter roll number to update: ")

            if roll_no not in school.student_list:
                print("Student not found")
                continue

            name = input("Enter new name: ")
            division = input("Enter new class division: ")
            branch = input("Enter new branch: ").lower().strip()

            if branch not in subject_branches:
                print("Invalid branch")
                continue

            student = Student(name, roll_no, division, branch)
            school.updating_student_accord(roll_no, student)

        elif choice == "5":
            roll_no = input("Enter roll number to delete: ")
            school.deleting_student(roll_no)

        elif choice == "6":
            roll_no = input("Enter roll number: ")

            try:
                school.average_marks(roll_no)
            except ValueError:
                print("Please enter valid numeric marks")

        elif choice == "7":
            school.save_records()

        elif choice == "0":
            print("Exiting program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()