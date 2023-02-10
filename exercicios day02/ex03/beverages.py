#!/usr/bin/env python3

class HotBeverage:
    def __init__(self):
        self.name = 'hot bavarage'
        self.price = 0.30

    def __str__(self):
        return f"{self.name}\n{self.price}\n{self.description()}"

    def description(self, description="Just some hot water in a cup"):
        return description


class Coffee(HotBeverage):

    def __init__(self):
        self.name = 'coffee'
        self.price = 0.40

    def description(self, description="A coffee, to stay awake."):
        return description

class Tea(HotBeverage):
    def __init__(self):
        self.name = 'tea'
        self.price = 0.30


class Chocolate(HotBeverage):
    def __init__(self):
        self.name = 'chocolate'
        self.price = 0.50

    def description(self, description="Chocolate, sweet chocolate."):
        return description


class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = 'cappuccino'
        self.price = 0.45

    def description(self, description="Un po’ di Italia nella sua tazza!"):
        return description


def print_drinks():
    hot_be = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    print(f'{hot_be}\n')
    print(f'{coffee}\n')
    print(f'{tea}\n')
    print(f'{chocolate}\n')
    print(f'{cappuccino}\n')


if __name__ == '__main__':
    print_drinks()