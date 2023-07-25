class College:
    def __init__(self):
        self.college_name = ""
        self.location = ""

    def InputCollegeData(self):
        self.college_name = input("enter college name")
        self.location = input("enter location")

    def DisplayCollegeDetails(self):
        print()
        print("***college details***")
        print("college name:", self.college_name)
        print("location:", self.location)
        print()


class Department(College):
    def __init__(self):
        super().__init__()
        self.department_id = ""
        self.department_name = ""
        self.HOD_name = ""

    def InputDepartmentData(self):
        self.department_id = input("enter department id")
        self.department_name = input("enter department name")
        self.HOD_name = input("enter HOD name")

    def DisplayDepartmentDetails(self):
        print()
        print("***Department details***")
        print("department id:", self.department_id)
        print("department id:", self.department_name)
        print("department id:", self.HOD_name)


class Student(Department):
    def __init__(self):
        super().__init__()
        self.student_name = ""
        self.student_roll_num = ""
        self.student_mobile = ""
        self.email = ""
        self.course = ""

    def InputStudentDAta(self):
        self.student_name = input("enter student name")
        self.student_roll_num = input("enter roll number")
        self.student_mobile = input("enter mobile number")
        self.email = input("enter email")
        self.course = input("enter course")

    def DisplayStudentDetails(self):
        print()
        print("***student details***")
        print("name:", self.student_name)
        print("roll number:", self.student_roll_num)
        print("mobile:", self.student_mobile)
        print("email:", self.email)
        print("course:", self.course)
        print()


obj1 = Student()
obj1.InputCollegeData()
obj1.InputDepartmentData()
obj1.InputStudentDAta()
obj1.DisplayCollegeDetails()
obj1.DisplayDepartmentDetails()
obj1.DisplayStudentDetails()
