from fastapi import FastAPI, Request
from config.database import database
from utils import uniqueShorts, is_valid_url, duplicateLink, redirectShorts
from request import ShortnerRequest
from fastapi.responses import RedirectResponse

app = FastAPI(
    # docs_url= None, 
    # redoc_url=None,
    )

@app.get('/')
def root():
    return RedirectResponse('https://google.com')

@app.get('/{short}')
async def links(short: str):
    return await redirectShorts(short)

@app.post('/shorten')
async def shorten_url(data: ShortnerRequest, request: Request):
    if is_valid_url(data.links):
        duplicate =  await duplicateLink(data.links, request)
        if duplicate:
            return duplicate
        short = await uniqueShorts()
        payload = {'key': short, 'link': data.links}
        if data.expiry:
            database.put(payload, expire_in=int(data.expiry))
            return f'{request.base_url}{short}'
        else:
            database.put(payload)
            return f'{request.base_url}{short}'

    return False
