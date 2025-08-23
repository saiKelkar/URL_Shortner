import random, string
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models import URLShorten
import schema

def generate_shorturl(length: int=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

def create_shorturl(url:schema.URLCreate, db:Session):
    while True:
        short_code = generate_shorturl()
        existing = db.query(URLShorten).filter(URLShorten.shortCode == short_code).first()
        if not existing:
            break

    new_url = URLShorten(
        url = url.url,
        shortCode = short_code,
        accessCount = 0
    )
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url

def get_url(shortCode:str, db:Session):
    url_long = db.query(URLShorten).filter(URLShorten.shortCode == shortCode).first()

    if not url_long:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Short URL not found")
    
    url_long.accessCount += 1
    db.commit()
    db.refresh(url_long)
    return url_long

def update_shorturl(id:int, url_update:schema.URLUpdate, db:Session):
    url_short = db.query(URLShorten).filter(URLShorten.id == id).first()
    if not url_short:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="ID not found")
    
    url_short.shortCode = url_update.shortCode
    
    db.commit()
    db.refresh(url_short)
    return url_short

def delete_url(id:int, db:Session):
    url = db.query(URLShorten).filter(URLShorten.id == id).first()
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"URL with ID {id} not found"
        )
    db.delete(url)
    db.commit()
    return { "message": f"URL with ID {id} deleted successfully" }

def get_stats(id:int, db:Session):
    stats = db.query(URLShorten).filter(URLShorten.id == id).first()
    if not stats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"URL with ID {id} not found"
        )
    
    return stats