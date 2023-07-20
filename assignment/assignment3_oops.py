# create a class that employee details:
# name, mobile,email,company,salary,location


class EmployeeDetails:
    def __init__(self, name, mobile, email, company, salary, location):
        self.Employee_name = name
        self.Employee_mobile = mobile
        self.Employee_email = email
        self.Employee_company = company
        self.Employee_salary = salary
        self.Employee_location = location

    def display_data(self):
        print("****Employee details****")
        print("name:", self.Employee_name)
        print("mobile:", self.Employee_mobile)
        print("email:", self.Employee_email)
        print("company:", self.Employee_company)
        print("salary:", self.Employee_salary)
        print("location:", self.Employee_location)
        print()


Employee1 = EmployeeDetails("maqswood", 8129599577, "maqswood1567@gmail.com", "luminar", 50000, "kakkanad")
Employee2 = EmployeeDetails("fayis", 7034511062, "fayis@gmail.com", "luminar2", 60000, "info park")

Employee1.display_data()
Employee2.display_data()
