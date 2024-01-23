# Дан класс корзина продуктов.
# реализовать сложение и вычитание из продуктов.
# В качестве корзины предусмотреть словарь, в который будут помещены продукты,
# Создаете 2 разных объекта, они должны складывать, вычитать.
# **Так же реализуйте бонусную систему.

class ProductBasket:
    def __init__(self):
        self.products = {}  # словарь для хранения продуктов в корзине

    def add_product(self, product, quantity):  # добавление продукта в корзину
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity):  # удаление продукта из корзины
        if product in self.products:
            if self.products[product] <= quantity:
                del self.products[product]
            else:
                self.products[product] -= quantity

    def show_products(self):  # вывод продуктов в корзине
        for product, quantity in self.products.items():
            print(f"{product}: {quantity}")


# User = ProductBasket()
# while True:
#     product = input("Enter: ")
#     if product == "":
#         break
#     else:
#         quantity = int(input(""))
#         User.add_product(product, quantity)

User.show_products()