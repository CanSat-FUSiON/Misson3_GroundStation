FROM python:3.9.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install -r requirements.txt
COPY . /app/
