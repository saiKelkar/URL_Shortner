from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# URLShorten
class URLCreate(BaseModel):
    url: str

class URLResponse(URLCreate):
    id: int
    shortCode: str
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    accessCount: int=0

class URLUpdate(BaseModel):
    shortCode: str