from fastapi import FastAPI, Request
from config.database import database
from utils import uniqueShorts, is_valid_url
from request import ShortnerRequest

app = FastAPI()

@app.get('/')
def root():
    return '__init__'

@app.post('/shorten')
async def shorten_url(data: ShortnerRequest, request: Request):
    if is_valid_url(data.links):
        short = uniqueShorts()
        payload = {'key': short, 'link': data.links}
        if database.put(payload, expire_in=3600):
            return f'{request.base_url}{short}'
        else:
            False