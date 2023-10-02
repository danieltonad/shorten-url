import random, string
from config.database import database
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
import re


async def redirectShorts(short: str):
    link = database.get(short)
    if link:
        return RedirectResponse(link['link'])
    return 'invalid link'


def is_valid_url(url):
    # Regular expression for a basic URL validation
    url_pattern = re.compile(r'^(https?|http)://[^\s/$.?#].[^\s]*$')
    return re.match(url_pattern, url) is not None

async def uniqueShorts():
    short = randomString()
    if database.get(short):
        return await uniqueShorts()
    else:
         return short

def randomString():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(3,6))

async def duplicateLink(link: str, request: Request):
    __ = database.fetch({'link': link})._items
    if __:
        short = __[0]
        return f'{request.base_url.fragment}{short["key"]}'
    else:
         return False