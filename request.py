from pydantic import BaseModel

class ShortnerRequest(BaseModel):
    links: str