import random, string
import validators
from config.database import database

def uniqueShorts():
    short = randomString(5)
    if database.get(short):
        return uniqueShorts()
    else:
         return short

def randomString(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))