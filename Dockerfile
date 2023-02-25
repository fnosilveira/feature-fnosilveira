FROM python:3.9

WORKDIR /src

COPY requirements.txt /src/requirements.txt

RUN pip install -r requirements.txt

COPY ./src /src

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
