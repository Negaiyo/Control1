# Дан класс корзина продуктов.
# реализовать сложение и вычитание из продуктов.
# В качестве корзины предусмотреть словарь, в который будут помещены продукты,
# Создаете 2 разных объекта, они должны складывать, вычитать.
# **Так же реализуйте бонусную систему.

from abc import abstractmethod


@abstractmethod
class basket:
    count = 0

    def __init__(self, product: dict):
        self.product = product