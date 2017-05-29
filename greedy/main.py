max_load = 10


class Container:
    def __init__(self, weight, price):
        self._weight = weight
        self._price = price

    @property
    def weight(self):
        return self._weight

    @property
    def price(self):
        return self._price

    def __str__(self):
        return 'Price: {}\tweight: {}'.format(self._price, self._weight)


class OverloadError(Exception):
    pass


class Load:
    def __init__(self, max_weight):
        self._load = []
        self._weight = 0
        self._max_weight = max_weight
        self._i = 0

    def add(self, element: Container):
        if element.weight + self._weight <= self._max_weight:
            self._load.append(element)
            self._weight += element.weight
        else:
            raise OverloadError

    @property
    def load(self):
        return self._load

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._load):
            to_return = self._load[self._i]
            self._i += 1
        else:
            raise StopIteration
        return to_return


class Dynamic:
    pass


class Greedy:
    _max_size = 0
    _containers = []

    @classmethod
    def choose(cls, max_size, containers):
        load = Load(max_size)
        cls._containers = containers

        sorted_containers = cls.sort_containers()
        for container in sorted_containers:
            try:
                load.add(container)
            except OverloadError:
                pass
        return load

    @classmethod
    def sort_containers(cls):
        return sorted(cls._containers, key=lambda element: element.price/element.weight, reverse=True)


containers = [
    Container(weight=1, price=1),
    Container(weight=2, price=5),
    Container(weight=3, price=2),
    Container(weight=6, price=3),
    Container(weight=4, price=3),
    Container(weight=2, price=2),
    Container(weight=3, price=4)
]


if __name__ == '__main__':
    for element in Greedy.choose(10, containers):
        print(element)
