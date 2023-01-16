class Tomato:
    states = {1: 'green', 2: 'yellow', 3: 'red'}

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        if self._index < 2:
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return "tomato ripe"
        else:
            return "tomato is not ripe"


class TomatoBush:

    def __init__(self, num):
        self.num = num
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for t in self.tomatoes:
            if t == 3:
                pass
            else:
                return t.grow()

    def all_are_ripe(self):
        counter = 0
        for t in self.tomatoes:
            if t.is_ripe():
                counter += 1
        return counter == self.num

    def giwe_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        return f"{self.name} poured tomatoes"

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.giwe_away_all()
            return "tomatoes are ripe and harvested"
        else:
            return "tomato is not ripe"

    @staticmethod
    def knowledge_base():
        print()


Gardener.knowledge_base()
t1 = TomatoBush(4)
g = Gardener("Teddy", t1)
print(g.work())
print(g.harvest())
print(g.work())
print(g.harvest())



