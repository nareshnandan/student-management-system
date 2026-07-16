import json

class StudentManagement:

    def __init__(self):
        self.file_name = "students.json"
        self.students = self.load_data()

    def load_data(self):
        try:
            with open(self.file_name,"r") as file:
                return json.load(file)
        except:
            return{}

    def save_data(self):
        with open(self.file_name, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):

        name = input("Enter Student Name : ")

        age = input("Enter Age : ")

        course = input("Enter Course : ")

        student_id = str(len(self.students) + 101)

        self.students[student_id] = {

            "name": name,

            "age": age,

            "course": course

        }

        self.save_data()

        print("\nStudent Added Successfully!")

        print("Student ID :", student_id)


    # def search_student(self):
    #     student_id = input("Enter Student ID : ")

    #     if student_id in self.students:

    #         student = self.students[student_id]

    #         print("\n===== Student Details =====")

    #         print("Student ID :", student_id)

    #         print("Name :", student["name"])

    #         print("Age :", student["age"])

    #         print("Course :", student["course"])

    #     else:

    #         print("Student Not Found!")
    def search_student(self):

        print("\n===== SEARCH STUDENT =====")
        print("1. Search by ID")
        print("2. Search by Name")
        print("3. Search by Course")

        choice = input("Enter Choice : ")

        if choice == "1":

            student_id = input("Enter Student ID : ")

            if student_id in self.students:
                student = self.students[student_id]

                print("\nStudent Found")
                print("Student ID :", student_id)
                print("Name :", student["name"])
                print("Age :", student["age"])
                print("Course :", student["course"])
            else:
                print("Student Not Found!")

        elif choice == "2":

            name = input("Enter Student Name : ").lower()

            found = False

            for student_id, student in self.students.items():

                if student["name"].lower() == name:

                    found = True

                    print("\nStudent ID :", student_id)
                    print("Name :", student["name"])
                    print("Age :", student["age"])
                    print("Course :", student["course"])

            if not found:
                print("Student Not Found!")

        elif choice == "3":

            course = input("Enter Course : ").lower()

            found = False

            for student_id, student in self.students.items():

                if student["course"].lower() == course:

                    found = True

                    print("\nStudent ID :", student_id)
                    print("Name :", student["name"])
                    print("Age :", student["age"])
                    print("Course :", student["course"])

            if not found:
                print("Student Not Found!")

        else:
            print("Invalid Choice!")

        def update_student(self):
            student_id = input("Enter Student ID : ")

            if student_id in self.students:

                self.students[student_id]["name"] = input("Enter New Name : ")

                self.students[student_id]["age"] = input("Enter New Age : ")

                self.students[student_id]["course"] = input("Enter New Course : ")

                self.save_data()

                print("Student Updated Successfully!")

            else:

                print("Student Not Found!")


    def delete_student(self):
        student_id = input("Enter Student ID : ")

        if student_id in self.students:

            del self.students[student_id]

            self.save_data()

            print("Student Deleted Successfully!")

        else:

            print("Student Not Found!")


    def view_student(self):
        student_id = input("Enter Student ID : ")

        if student_id in self.students:

            student = self.students[student_id]

            print("\n===== STUDENT DETAILS =====")

            print("Student ID :", student_id)
            print("Name :", student["name"])
            print("Age :", student["age"])
            print("Course :", student["course"])

        else:

            print("Student Not Found!")


    def view_all_students(self):
        if len(self.students) == 0:
            print("No Students Found!")
        else:
            print("\n===== ALL STUDENTS =====")

            for student_id, student in self.students.items():

                print("----------------------------")

                print("Student ID :", student_id)
                print("Name :", student["name"])
                print("Age :", student["age"])
                print("Course :", student["course"])


    def main_menu(self):
        while True:

            print("\n===== STUDENT MANAGEMENT SYSTEM =====")

            print("1. Add Student")
            print("2. Search Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. View Student")
            print("6. View All Students")
            print("7. Exit")

            choice = input("Enter Choice : ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.search_student()

            elif choice == "3":
                self.update_student()

            elif choice == "4":
                self.delete_student()

            elif choice == "5":
                self.view_student()

            elif choice == "6":
                self.view_all_students()

            elif choice == "7":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")


student = StudentManagement()
student.main_menu()

