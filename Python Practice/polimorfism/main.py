from university import University
from college import College
from student import Student

# Child Class
if __name__ == "__main__":
    # Creating an instance of the Student class
    university = University(uni_name = "Lancaster University.", uni_location="Lancaster.")
    college = College(uni_name="Lancaster University.", uni_location="Lancaster.", college_name="Computing and Comminication College.", college_location="Info21 Tower.")
    student = Student(uni_name="Lancaster University.", uni_location="Lancaster.", college_name="Computing and Comminication College.", college_location="Info21 Tower.", student_name="Pankaj Dilip Goikar.", student_id="007.")

    # PolyMorfism in action. The display_info method is called on each object.
    object_list = [university, college, student]
    
    for obj in object_list:
        obj.display_info()
        print("-" * 50)