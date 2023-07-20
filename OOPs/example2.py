class StudentsDetails:
    def __init__(self, name, age):
        self.Student_name = name
        self.Student_age = age

    def display_data(self):
        print("****student details****")
        print(self.Student_name, self.Student_age)
        print()


student1 = StudentsDetails("maqswood", 20)
student2 = StudentsDetails("fayis", 22)

student1.display_data()
student2.display_data()
