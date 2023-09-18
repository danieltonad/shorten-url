from fastapi import FastAPI
from config.database import database

app = FastAPI()

@app.get('/')
def root():
    return '__init__'

@app.grt('/{url}')
async def shorten_url(url: str):
    
    database.