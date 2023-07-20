class StudentsDetails:
    def __init__(self):
        self.Student_name = ""
        self.Student_age = ""
        self.Student_place = ""

    def Data_input(self):
        self.Student_name = input("enter your name")
        self.Student_age = input("enter your age")
        self.Student_place = input("enter your place")

    def DisplayDetails(self):
        print("***student details***")
        print("name:", self.Student_name)
        print("age:", self.Student_age)
        print("place:", self.Student_place)


student1 = StudentsDetails()
student2 = StudentsDetails()
student1.Data_input()
student1.DisplayDetails()
