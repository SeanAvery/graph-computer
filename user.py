from time import sleep
from threading import Thread

class User(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while(True):
            sleep(2)
            print('sending transaction')

for i in range(100):
    user = User()
    user.start()
