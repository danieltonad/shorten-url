from pydantic import BaseModel
from typing import Optional

class ShortnerRequest(BaseModel):
    links: str
    expiry: Optional[str] = None