# create class that display area rectangle
class Rectangle1:
    def __init__(self, l, w):
        self.Length = l
        self.Width = w

    def Rect_Area(self):
        print("Area of rectangle=", self.Length * self.Width)


Area = Rectangle1(2, 4)
Area2 = Rectangle1(23, 12)
Area.Rect_Area()
Area2.Rect_Area()
