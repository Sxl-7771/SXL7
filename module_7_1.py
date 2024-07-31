class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products: Product):
        current_names = set(
            line.split(', ')[0] for line in self.get_products().splitlines()
        )

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name in current_names:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(f'{product}\n')
                    current_names.add(product.name)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
