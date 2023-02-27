FROM python:3.11-alpine

WORKDIR /app

RUN python3 -m pip install --upgrade pip

COPY . .

RUN python3 -m pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app"

CMD ["python3", "app.py"]
