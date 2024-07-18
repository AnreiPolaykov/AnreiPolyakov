class Product():
    def __init__(self, name: str, weight: float,  category: str ): #создаём атрибуты для класса Product
        self.name = name # имя
        self.weight = weight #вес
        self.category = category #категория

    def __str__(self): #возвращаем все атрибуты класса в виде строки
        return f"{self.name}, {self.weight},{self.category}"

class Shop():

    __file_name = 'products.txt' # создаём атрибут  для работы с текстовым файлом

    def get_product(self): #Метод считывает всю информацию из файла __file_name
        with open(self.__file_name, 'r') as file: #открываем файл для чтения
            products = file.read() #переписываем данные из __file_name в products
            file.close() #закрываем его
        return products #возвращаем единую строку со всеми товарами из файла __file_name


    def add(self, *products):# Метод который принимает неограниченное количество объектов класса
        vse_products = self.get_product()# vse_products принимает значение метода get_product
        with open(self.__file_name, 'a') as file:#открываем __file_name для добавления в атрибутов в products.txt
            for i in products:#ищем i в строке products
                if i.name in vse_products:#ищем имя в списке
                    print(f"Продукт {i.name} уже есть в магазине")
                else:
                    vse_products +=str(i) + '\n'# если не находим добавляем данные о продукте в список
                    file.write(str(i) + '\n')





s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_product())
