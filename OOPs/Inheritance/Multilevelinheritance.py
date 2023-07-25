class FirstClasss:
    def Function1(self):
        print("inside first class")


class SecondClass(FirstClasss):
    def Function2(self):
        print("inside second class")


class ThirdClass(SecondClass):
    def Function3(self):
        print("inside Third class")


obj1 = ThirdClass()
obj1.Function3()
obj1.Function2()
obj1.Function1()
