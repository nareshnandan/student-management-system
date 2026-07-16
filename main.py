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
        pass

student = StudentManagement()
student.main_menu()

