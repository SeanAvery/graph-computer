import os
import codecs
import random

class State():
    def __init__(self, genesis):
        self.state = genesis
        self.pool = []

    def submit_transaction(self, transaction):
        # case 1: pool is empty
        if len(self.pool) == 0:
            self.pool.append(transaction)

        # case 2: insert by price priority
        found_insert_location = False
        for i, tx in enumerate(self.pool):
            # if gas price is higher
            if tx[1] > transaction[1]:
                # insert behind higher priced transaction
                self.pool.insert(i, transaction)
                # we are done
                found_insert_location = True
                break

        # case 3: transaction is the hghest price
        if found_insert_location != True:
            self.pool.append(transaction)

    def create_random_transaction(self):
        # random id hash
        id = codecs.encode(os.urandom(32), 'hex').decode()
        # random gas price
        gas_price = random.randint(0, 999)

        return (id, gas_price)

### testing!

# genesis is a random 32 byte
genesis = codecs.encode(os.urandom(32), 'hex').decode()
state = State(genesis)
for i in range(100):
    transaction = state.create_random_transaction()
    state.submit_transaction(transaction)
print(state.pool)
