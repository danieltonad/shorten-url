from pydantic import BaseModel

class Shortner(BaseModel):
    links: str