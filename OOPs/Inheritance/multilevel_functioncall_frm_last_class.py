class hosptl:
    def __init__(self):
        self.hname = ""
        self.hplace = ""
        self.hnumber = ""

    def inp_hsptl(self):
        self.hname = input("enter hsptl name")
        self.hplace = input("enter hsptl place")
        self.hnumber = input("enter hsptl number")

    def display_hsptl(self):
        print("****hospital detail***")
        print("Hospital name:", self.hname)
        print("Hospital place:", self.hplace)
        print("Hospital number:", self.hnumber)


class section(hosptl):
    def __init__(self):
        self.section = ""
        self.doctor = ""

    def inp_section(self):
        obj.inp_hsptl()
        self.section = input("enter section name")
        self.doctor = input("enter doctor name")

    def display_section(self):
        obj.display_hsptl()
        print("****department detail***")
        print("department name:", self.section)
        print("doctor name:", self.doctor)


class patient(section):
    def __init__(self):
        self.pname = ""
        self.page = ""
        self.pnumber = ""

    def inp_patient(self):
        obj.inp_section()
        self.pname = input("enter patient name")
        self.page = input("enter patient age")
        self.pnumber = input("enter patient number")

    def display_patient(self):
        obj.display_section()
        print("****patient detail***")
        print("patient name:", self.pname)
        print("patient age:", self.page)
        print("patient number:", self.pnumber)


obj = patient()
obj.inp_patient()
obj.display_patient()
