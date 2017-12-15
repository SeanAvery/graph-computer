import random
import codecs
import os

def create_random_account():
    return codecs.encode(os.urandom(16), 'hex').decode()

def create_random_weight():
    return random.randint(0, 999)
