from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schema
from database import get_db
from controllers import shortencontrollers

router = APIRouter(prefix="/shorten", tags=["URLShorten"])

# Create a new short URL
@router.post("/", response_model=schema.URLResponse)
def createShortURL(url:schema.URLCreate, db:Session=Depends(get_db)):
    return shortencontrollers.create_shorturl(url, db)

# Get original URL from the short URL
@router.get("/{shortCode}", response_model=schema.URLResponse)
def getURL(shortCode:str, db:Session=Depends(get_db)):
    return shortencontrollers.get_url(shortCode, db)

# Update the existing short URL
@router.put("/{id}", response_model=schema.URLResponse)
def updateShortURL(id:int, url_update:schema.URLUpdate, db:Session=Depends(get_db)):
    return shortencontrollers.update_shorturl(id, url_update.shortCode, db)

# Delete short URL
@router.delete("/{id}")
def deleteURL(id:int, db:Session=Depends(get_db)):
    return shortencontrollers.delete_url(id, db)

# Get statistics on short URL (no. of time accessed)
@router.get("/{id}/stats", response_model=schema.URLResponse)
def getStats(id:int, db:Session=Depends(get_db)):
    return shortencontrollers.get_stats(id, db)