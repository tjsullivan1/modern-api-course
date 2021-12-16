from typing import Optional
from pydantic import BaseModel

from datetime import datetime
from models.location import Location

class ReportSubmittal(BaseModel):
    description: str
    location: Location


class Report(ReportSubmittal):
    id: str
    created_date: Optional[datetime]