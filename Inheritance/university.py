class University:
    def __init__(self, uni_name, uni_location):
        self.uni_name = uni_name
        self.uni_location = uni_location
    
    def display_uni_info(self):
        print("University Information:")
        print(f"University Name: {self.uni_name}")
        print(f"University Location: {self.uni_location}")
    
    def import_data(self, path):
        with open(path, 'r') as f:
            data = f.read()
        return data
    
    def cal_mean(self, data):
        data = data.split()
        data = [int(i) for i in data]
        return sum(data)/len(data)