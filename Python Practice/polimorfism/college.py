from university import University

class College(University):
    def __init__(self, uni_name, uni_location, college_name, college_location):
        super().__init__(uni_name, uni_location)
        self.college_name = college_name
        self.college_location = college_location

    def display_info(self):         # Polimorfism method. Overriding the display_info method from the parent class.
        print("College Information:")
        print(f"College Name: {self.college_name}")
        print(f"College Location: {self.college_location}")