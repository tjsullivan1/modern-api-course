from typing import Optional
from pydantic import BaseModel

from datetime import datetime
from models.location import Location

class Report(BaseModel):
    description: str
    location: Location
    created_date: Optional[datetime]