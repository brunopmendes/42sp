import random
from beverages import *


class CoffeeMachine:
    
    def __init__(self):
        self.status_machine = True
        self.broken_counter = 0
        
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.price=0.90 
            self.name='empty cup'

        def description(self):
            return "An empty cup?! Gimme my nomey back"

    class BrokenMachineException(Exception):
        def __init__(self, message='This coffee machine has to be repaired'):
            self.message = message
            super().__init__(self.message)

    def repair(self):
        self.status_machine = True
        self.broken_counter = 0
        # raise self.BrokenMachineException()

    def serve(self, beverage):
        if self.broken_counter == 10:
            self.status_machine = False
            raise self.BrokenMachineException()

        self.broken_counter += 1

        return random.choice((beverage, self.EmptyCup()))

if __name__ == '__main__':
    machine = CoffeeMachine()                            

    drinks = (Chocolate(), Tea(), Cappuccino(), Coffee())

    attempts = 2

    while attempts > 0:
        try:
            while machine.status_machine:
                print(f'{machine.serve(random.choice(drinks))}\n')
        except Exception as e: 
            print(e, '\n\n')
            machine.repair()
        finally:
            attempts -= 1
