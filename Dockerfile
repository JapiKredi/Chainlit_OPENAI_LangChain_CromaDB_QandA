FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["chainlit", "run", "app2.py", "--host=0.0.0.0", "--port=80", "--headless"]
