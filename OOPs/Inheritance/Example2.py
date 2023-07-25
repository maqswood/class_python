class Teacher:
    def __init__(self):
        self.teacher_name = ""
        self.subject = ""

    def InputTeacherdata(self):
        self.teacher_name = input("enter teacher name")
        self.subject = input("enter subject name")

    def DisplayTeacherdetails(self):
        print()
        print("***teacher details***")
        print("name:", self.teacher_name)
        print("Subject:", self.subject)
        print()


class student(Teacher):
    def __init__(self):
        self.student_name = ""
        self.age = ""
        self.course = ""

    def InputStudentDAta(self):
        self.student_name = input("enter student name")
        self.age = input("enter age")
        self.course = input("enter course")

    def DisplayStudentDetails(self):
        print("***student details***")
        print("name:", self.student_name)
        print("age:", self.age)
        print("course:", self.course)
        print()


obj1 = student()
obj1.InputTeacherdata()
obj1.InputStudentDAta()
obj1.DisplayTeacherdetails()
obj1.DisplayStudentDetails()
