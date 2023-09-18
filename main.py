from fastapi import FastAPI, Request
from config.database import database
from utils import uniqueShorts
from http import HTTPStatus

app = FastAPI()

@app.get('/')
def root():
    return '__init__'

@app.get('/shorten/{url}')
async def shorten_url(url: str, request: Request):
    short = uniqueShorts()
    payload = {'key': short, 'link': url}
    if database.put(payload, expire_in=3600):
        return f'{request.base_url}{short}'
    else:
        False