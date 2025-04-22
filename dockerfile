#FROM python:3.13-slim
#FROM python:3.13-slim-bullseye
FROM python:3-alpine
RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev \
            wget

RUN apk add --no-cache pcre

WORKDIR /app
COPY requirements.txt requirements.txt
COPY . .
#COPY ./requirements.txt /app

RUN pip install -r requirements.txt

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
# Download prices.txt file from the GitHub repository
#RUN apt-get update && apt-get install -y wget && \
 RUN   wget -O prices.txt https://raw.githubusercontent.com/amaryeh/my_docker_app/main/prices.txt
# Expose the port the app runs on
EXPOSE 5000
#CMD ["python", "app.py"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]


