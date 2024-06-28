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



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
