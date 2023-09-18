from fastapi import FastAPI, Request
from config.database import database
from utils import uniqueShorts, is_valid_url

app = FastAPI()

@app.get('/')
def root():
    return '__init__'

@app.post('/shorten/{url}')
async def shorten_url(data: dict, request: Request):
    if is_valid_url(data.):
        return True
    # short = uniqueShorts()
    # payload = {'key': short, 'link': url}
    # if database.put(payload, expire_in=3600):
    #     return f'{request.base_url}{short}'
    # else:
    #     False