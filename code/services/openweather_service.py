from typing import Optional
import httpx
from infrastructure import weather_cache

api_key: Optional[str] = None

async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if forecast := weather_cache.get_weather(city, state, country, units):
        return forecast

    if state:
        query = f'{city},{state},{country}'
    else:    
        query = f'{city},{country}'
        
    url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&APPID={api_key}&units={units}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        forecast = resp.json()['main']

        weather_cache.set_weather(city, state, country, units, forecast)
        
        return forecast