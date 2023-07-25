class vehicle:
    def function1(self):
        print("Inside parent class")


class car(vehicle):
    def function2(self):
        print("inside car")


class truck(vehicle):
    def function3(self):
        print("inside truck")


class bike(vehicle):
    def function4(self):
        print("inside bike")


obj=car()
obj.function1()
obj.function2()

obj1=truck()
obj1.function1()
obj1.function3()

obj2=bike()
obj2.function1()
obj2.function4()
