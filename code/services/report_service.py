from datetime import datetime
from typing import List
from models.location import Location
from models.reports import Report
import uuid

__reports = []

async def get_reports() -> List[Report]:
    # would add an async call here.
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.now()
    report = Report(id=str(uuid.uuid4()), location=location, description=description, created_date=now)

    # would add an async call here
    __reports.append(report)
    __reports.sort(key=lambda r: r.created_date, reverse=True)

    return report