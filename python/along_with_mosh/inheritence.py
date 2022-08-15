class Human():
        legs = 2
        ears = 2

class Student(Human):
    def __init__(self,id,classRoom):
        self.id = id
        self.classRoom = classRoom
ranga = Student(174,9)
print(ranga.legs)

ranga.age = 45
print(ranga.age)