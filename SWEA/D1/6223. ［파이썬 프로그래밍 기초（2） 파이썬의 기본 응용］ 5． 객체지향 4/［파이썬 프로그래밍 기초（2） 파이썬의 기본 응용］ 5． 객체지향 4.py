import math

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self.print_result()
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        self._radius = value
        
    def get_area(self):
        area = math.pi * (self._radius ** 2)
        return math.floor(area * 100) / 100
    
    def print_result(self):
        print(f"원의 면적: {self.get_area()}")
        
r = 2.0
Circle(r)