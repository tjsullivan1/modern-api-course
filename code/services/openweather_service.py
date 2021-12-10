from typing import Optional
import httpx

api_key: Optional[str] = None

async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        query = f'{city},{state},{country}'
    else:    
        query = f'{city},{country}'
        
    url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&APPID={api_key}&units={units}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data['main']
    
    return forecast