from fastapi import FastAPI
app = FastAPI()

@app.get('/')

def reet():
    return '__init__'
