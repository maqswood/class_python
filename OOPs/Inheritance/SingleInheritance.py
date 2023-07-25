class MainClasss:
    def Function1(self):
        print("inside amin class")


class ChildClass(MainClasss):
    def Function2(self):
        print("inside sub class")


obj1 = ChildClass()
obj1.Function1()
obj1.Function2()
