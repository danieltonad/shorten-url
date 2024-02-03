import random, string
from config.database import database
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
import re
from bson import ObjectId
import requests

async def redirectShorts(short: str):
    link = database.find_one({'key':short})
    print(link)
    if link:
        return RedirectResponse(link['link'])
    return 'invalid link'


def is_valid_url(url):
    # Regular expression for a basic URL validation
    url_pattern = re.compile(r'^(https?|http)://[^\s/$.?#].[^\s]*$')
    return re.match(url_pattern, url) is not None

async def uniqueShorts():
    short = randomString()
    if database.find_one({'key':short}):
        return await uniqueShorts()
    else:
         return short

def randomString():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(3,6))

async def duplicateLink(link: str, request: Request):
    __ = database.find_one({'link': link})
    if __:
        return f'{request.base_url.hostname}/{__.get("key")}'
    else:
         return False
     
     
async def get_ip_address():
    try:
        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:
            ip_address = response.json().get('origin', '')
            print(ip_address)
            return ip_address
        else:
            print(f"Failed to retrieve IP address. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None