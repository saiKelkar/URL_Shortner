from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from database import Base

class URLShorten(Base):
    __tablename__ = "urlshorten"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    shortCode = Column(String)

    createdAt = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=True
    )
    updatedAt = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True
    )

    accessCount = Column(Integer)