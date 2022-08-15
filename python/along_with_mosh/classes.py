# class Point():
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print('draw')

# point1 = Point()
# point1.draw()


class Person():
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print('hey i am ',self.name)

person1 = Person('sai')

person1.talk()


