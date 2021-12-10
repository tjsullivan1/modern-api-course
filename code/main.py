from pathlib import Path
from typing import Optional

import fastapi
import json
import uvicorn
from fastapi.staticfiles import StaticFiles

from api import weather_api
from views import home
from services import openweather_service

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found. You cannot continue -- please see settings_Template.json")
        raise Exception("settings.json file not found. You cannot continue -- please see settings_Template.json")
    
    with open('settings.json') as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get('api_key')
    

if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()