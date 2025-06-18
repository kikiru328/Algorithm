class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.print_result()
        
    def get_area(self):
        return self._width * self._height
    
    def print_result(self):
        print(f"사각형의 면적: {self.get_area()}")

Rectangle(4, 5)