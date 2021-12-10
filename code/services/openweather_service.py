from typing import Optional

api_key: Optional[str] = None

def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    query = f'{city},{country}'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&APPID={api_key}'
    
    return url