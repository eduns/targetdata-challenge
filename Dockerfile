FROM python:3.9-slim

WORKDIR /api
COPY src /api
COPY requirements.txt /api
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8080"]