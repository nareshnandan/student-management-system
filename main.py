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
        pass

    def search_student(self):
        pass

    def update_student(self):
        pass

    def delete_student(self):
        pass

    def view_student(self):
        pass

    def view_all_students(self):
        pass

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

