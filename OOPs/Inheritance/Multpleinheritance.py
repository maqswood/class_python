class a:
    def function1(self):
        print("inside class a")


class b:
    def function2(self):
        print("inside class b")


class c(a,b):
    def function3(self):
        print("inside class c")

obj=c()
obj.function1()
obj.function2()
obj.function3()