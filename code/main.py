from typing import Optional
import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def index():
    body = "<html>" \
                "<body>" \
                "<h1>Welcome to the API</h1>" \
                "</body>" \
            "</html>" \

    return fastapi.responses.HTMLResponse(body)

@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
            status_code=400,
            content='{"Error": "Z cannot be zero"}'
            )
    value = (x + y)

    if z is not None:
        value /= z

    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }


uvicorn.run(api)
