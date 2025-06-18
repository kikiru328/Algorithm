class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

def print_gender(person: Person):
    print(person.getGender())

print_gender(Male())
print_gender(Female())
