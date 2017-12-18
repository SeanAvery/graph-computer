from threading import Thread
from time import sleep

class ValidatorClient(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            sleep(2)
            print('validator is making decision')
