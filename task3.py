# Реализовать на свободную темы все концепции ООП, соединенные единым смыслом.
from abc import abstractmethod


@abstractmethod
class Animal:
    def __init__(self, land,
                 flying):
        self.land = land
        self.flying = flying


class Dog(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = 'Dog'
        self.weight = 20
        self.food = 'Bone'
        self.flying = False
        self.name = name

    def roar(self):
        print("GAF")


class Bird(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = 'Bird'
        self.weight = 5
        self.food = 'Grains'
        self.flying = True
        self.name = name

    def whistling(self):
        print("PIPIPI")
