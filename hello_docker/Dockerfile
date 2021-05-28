FROM python:3.8-alpine

COPY . /app/

RUN  pip install --upgrade pip

RUN pip install -r /app/requirements.txt

WORKDIR /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
