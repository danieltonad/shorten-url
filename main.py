from fastapi import FastAPI
from config.database import database
from utils import uniqueShorts

app = FastAPI()

@app.get('/')
def root():
    return '__init__'

@app.grt('/shorten/{url}')
async def shorten_url(url: str):
    payload = 
    database.