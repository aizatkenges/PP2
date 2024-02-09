class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

if __name__ == "__main__":
    
    shape = Shape()
    print("Area of the shape:", shape.area())  # Output will be 0

    
    square = Square(4)
    print("Area of the square:", square.area())  # Output will be 16
