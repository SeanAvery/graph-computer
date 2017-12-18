import os
import codecs

class State():
    def __init__(self, genesis):
        print('yu, created state XD')
        self.state = genesis
        print(self.state)
        self.pool = []

### testing!

# genesis is a random 32 byte
genesis = codecs.encode(os.urandom(32), 'hex').decode()
state = State(genesis)
