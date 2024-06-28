class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):

        if 1 > int(new_floor) or int(new_floor) > int(self.number_of_floors):
            print("Такого этажа не существует")
            return
        else:
            new_floor_list = list(range(1, new_floor + 1))
            for i in new_floor_list:
                print(i)

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей:{self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)


print(len(h1))
print(len(h2))