# урок 6.1 наследование классов
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


# лекция
# class Human:
#     head = True
#
#     def say_hello(self):
#         print('Здравствуйте')
#
#     # def __init__(self):
#     #     self.about()
#
# class Student(Human):
#     head = False
#
#     def about(self):
#         print('Я студент')
#
#     def say_hello(self):
#         print('Здравствуйте')
#
# class Teacher(Human):
#     pass
#
# # human = Human()
# student = Student()
# teacher = Teacher()
# student.say_hello()
# teacher.say_hello()
# # print(human.head)
# # student.about()
# print(student.head)
# # human.about()
