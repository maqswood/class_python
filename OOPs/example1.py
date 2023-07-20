class students_details:
    def __init__(self, name, age):
        self.Student_name = name
        self.Student_age = age


student1 = students_details("maqswood", 20)
student2 = students_details("fayis", 22)

print(student1.Student_name, student1.Student_age)
