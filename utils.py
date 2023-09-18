import random, string
from config.database import database
import re

def is_valid_url(url):
    # Regular expression for a basic URL validation
    url_pattern = re.compile(r'^(https?|http)://[^\s/$.?#].[^\s]*$')
    return re.match(url_pattern, url) is not None

def uniqueShorts():
    short = randomString(5)
    if database.get(short):
        return uniqueShorts()
    else:
         return short

def randomString(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))