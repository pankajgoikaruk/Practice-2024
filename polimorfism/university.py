class University:
    def __init__(self, uni_name, uni_location):
        self.uni_name = uni_name
        self.uni_location = uni_location
    
    def display_info(self):          # Polimorfism method
        print("University Information:")
        print(f"University Name: {self.uni_name}")
        print(f"University Location: {self.uni_location}")