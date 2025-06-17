class Student:
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
        
class GraduateStudent(Student):
    def __init__(self, name: str, major: str):
        super().__init__(name)
        self._major = major
        
    @property
    def major(self):
        return self._major
    
    @major.setter
    def major(self, value: str):
        self._major = value
        
s1 = Student("홍길동")
print(f"이름: {s1.name}")
s2 = GraduateStudent("이순신", "컴퓨터")
print(f"이름: {s2.name}, 전공: {s2.major}")
        