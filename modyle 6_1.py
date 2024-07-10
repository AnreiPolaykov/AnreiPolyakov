class Animal():
    def __init__(self,name):
        self.alive = True
        self.fed = False
        self.name = name

class Mamal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{food.name} не стал есть {self.name} ")
            self.alive = False
class Predator(Animal):
    def eat(self,food):
         if food.edible:
            print(f"{self.name} не стал есть {food.name}")
            self.fed = False
         else:
            print(f"{food.name} съел {self.name} ")
            self.alive = False


class Plant():
    def __init__(self,name):
        self.edible = False
        self.name = name

class Flower(Plant):
    Plant.edible = True
class Fruit(Plant):
        def __init__(self, name):
            self.name = name
            self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mamal('Хатико')
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