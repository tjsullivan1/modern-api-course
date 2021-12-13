from typing import Optional, Tuple
import httpx
from models.validation_error import ValidationError
from infrastructure import weather_cache

api_key: Optional[str] = None

async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    city, state, country, units = validate_inputs(city, state, country, units)
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
        if resp.status_code != 200:
            raise ValidationError(resp.text, status_code=resp.status_code)

        forecast = resp.json()['main']

        weather_cache.set_weather(city, state, country, units, forecast)
        
        return forecast


def validate_inputs(city: str, state: Optional[str], country: Optional[str], units: str) -> Tuple[str, Optional[str], str, str]:
    
    city = city.lower().strip()

    if not country:
        country = "us"
    else:
        country = country.lower().strip()

    if len(country) != 2:
        error = f"Invalid country input: {country}. This must be a two letter abbrevitaion such as US or GB."
        raise ValidationError(status_code=400, error_msg=error)

    if state:
        state = state.strip().lower()

    if state and len(state) != 2:
        error = f"Invalid state: {state}. It must be a two letter abbreviation, such as MN or WI."
        raise ValidationError(status_code=400, error_msg=error)

    if units:
        units = units.strip().lower()

    valid_units = {'standard', 'metric', 'imperial'}
    if units not in valid_units:
        error = f"invalid units '{units}', it must be one of {valid_units}"
        raise ValidationError(status_code=400, error_msg=error)

    return city, state, country, units
