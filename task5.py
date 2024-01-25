class Tomato:
    states = ["Посажен", "Растёт", "Вырос"]

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        if self._state != self.states[-1]:
            _index = self.states.index(self._state)
            self._state = self.states[_index + 1]

    def is_ripe(self):
        if self._state == Tomato.states[2]:
            print("Томат созрел!")
        else:
            print("Ещё нужно подождать)")


class TomatoBush(Tomato):

    def __init__(self, count):
        super().__init__()
        self.tomatoes = [(Tomato(i) for i in range(1, count + 1))]

    def grow_all(self):
        _index = self.states.index(self._state)
        for i in range(self.tomatoes):
            self._state = self.states[_index + 1]

    def all_are_ripe(self):
        if len(set(self.tomatoes)) == 1:
            print("Все томаты выросли")

    def give_away_all(self):
        self.tomatoes.clear()
        print("Все томаты собраны!")


class Gardener(Tomato):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self._plant = Tomato.states

    def work(self):
        pass
