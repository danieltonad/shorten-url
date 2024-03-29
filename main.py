from fastapi import FastAPI, Request
from config.database import database
from utils import uniqueShorts, is_valid_url, duplicateLink, redirectShorts, get_ip_address
from request import ShortnerRequest
from fastapi.responses import RedirectResponse
from mangum import Mangum


app = FastAPI(
    # docs_url= None, 
    # redoc_url=None,
    )

handler = Mangum(app)

@app.get('/')
async def root():
    # return RedirectResponse('https://google.com')
    return await get_ip_address()

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
        resp = database.insert_one(payload)
        return f'{request.base_url}{short}'

    return False
