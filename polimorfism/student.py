from college import College  # Import the College class from the college module

class Student(College):  # Inheriting from the College class
    def __init__(self, uni_name, uni_location, college_name, college_location, student_name, student_id):
        super().__init__(uni_name, uni_location, college_name, college_location)  # Calling the constructor of the parent class
        self.student_name = student_name
        self.student_id = student_id

    def display_info(self):     # Polimorfism method. Overriding the display_info method from the parent class.
        # Accessing attributes from the parent class
        print("Student Information:")        
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")
