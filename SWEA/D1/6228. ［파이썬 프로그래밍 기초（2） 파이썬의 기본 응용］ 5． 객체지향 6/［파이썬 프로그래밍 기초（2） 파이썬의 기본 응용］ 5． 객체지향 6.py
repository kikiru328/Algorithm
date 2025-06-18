class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self._length = length
        self.print_result()
    
    def area(self):
        return self._length ** 2
    
    def print_result(self):
        print(f"정사각형의 면적: {self.area()}")
        
Square(3)