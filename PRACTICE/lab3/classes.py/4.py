class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    # Creating a Rectangle object with length 5 and width 3
    rectangle = Rectangle(5, 3)
    print("Area of the rectangle:", rectangle.area())  # Output will be 15
