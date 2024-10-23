# syntax=docker/dockerfile:1

FROM python:3.10-slim
WORKDIR /server
RUN pip3 install -r requirements.txt
COPY . .
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "app:app"]
