import requests
from reportapp import report_event

events = [
    {"description": "heavy rain", "city": "Seattle", "state": "WA" },
    {"description": "very hot", "city": "New Prague", "state": "MN" },
    {"description": "snow", "city": "Land O Lakes", "state": "WI" },
    {"description": "fog", "city": "Seth", "state": "WV" },
    {"description": "blizzard", "city": "Iron Mountain", "state": "MI" },
]

def main():
    for event in events:
        report_event(description=event.get("description"), city=event.get("city"), state=event.get("state"))


if __name__ == '__main__':
    main()