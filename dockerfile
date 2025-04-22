FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Download prices.txt file from the GitHub repository
RUN apt-get update && apt-get install -y wget && \
    wget -O prices.txt https://raw.githubusercontent.com/amaryeh/my_docker_app/main/prices.txt
# Expose the port the app runs on
EXPOSE 5000
CMD ["python", "app.py"]

