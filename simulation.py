from time import sleep
from validator import Validator
from utils import create_random_account, create_random_weight

class Simulation():
    def __init__(self):
        self.validators = set()
        print('starting simulation')
        sleep(2)

    def create_validators(self):
        for _ in range(10):
            id = create_random_account()
            weight = create_random_weight()
            self.validators.add(Validator(id, weight))

def main():
    simulation = Simulation()
    simulation.create_validators()

if __name__ == '__main__':
    main()
