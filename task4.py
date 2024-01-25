# Дан класс корзина продуктов.
# реализовать сложение и вычитание из продуктов.
# В качестве корзины предусмотреть словарь, в который будут помещены продукты,
# Создаете 2 разных объекта, они должны складывать, вычитать.
# **Так же реализуйте бонусную систему.

class ProductBasket:
    def __init__(self):
        self.products = {}  # словарь для хранения продуктов в корзине
        self.price = []  # список для цены

    def add_product(self, product, quantity, price):  # добавление продукта в корзину
        if product in self.products:
            self.products[product] += quantity
            self.price.append(price)
        else:
            self.products[product] = quantity
            self.price.append(price)

    def remove_product(self, product, quantity):  # удаление продукта из корзины
        if product in self.products:
            if self.products[product] <= quantity:
                del self.products[product]
            else:
                self.products[product] -= quantity

    def show_products(self):  # вывод продуктов в корзине
        for product, quantity in self.products.items():
            print(f"{product}: {quantity}")

    def bonus(self):
        return (f"Ваше кол-во бонусов = {sum(self.price) * 2 / 100}")  # Вывод бонусов


User = ProductBasket()
User.add_product("Apple", 5, 30)
User.add_product("Banana", 2, 10)
print(User.bonus())
# while True:
#     product = input("Enter: ")
#     if product == "":
#         break
#     else:
#         quantity = int(input(""))
#         User.add_product(product, quantity)

User.show_products()
