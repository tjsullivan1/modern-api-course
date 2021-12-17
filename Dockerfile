FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements

RUN pip install --no-cache-dior --upgrade -r /code/requirements.txt

COPY ./code /code/app

CMD ["uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "80"]