from college import College  # Import the College class from the college module

class Student(College):  # Inheriting from the College class
    def __init__(self, uni_name, uni_location, college_name, college_location, student_name, student_id):
        super().__init__(uni_name, uni_location, college_name, college_location)  # Calling the constructor of the parent class
        self.student_name = student_name
        self.student_id = student_id

    def display_student_info(self):
        # Accessing attributes from the parent class
        print("Student Information:")        
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")

# Child Class
if __name__ == "__main__":
    # Creating an instance of the Student class
    student = Student(uni_name="Lancaster University.", uni_location="Lancaster.", college_name="Computing and Comminication College.", college_location="Info21 Tower.", student_name="Pankaj Dilip Goikar.", student_id="007.")

    # Calling the display_student_info method
    student.display_student_info()
    student.display_college_info()
    student.display_uni_info()
    # student.import_data("data.txt")
    # student.cal_mean(data)
