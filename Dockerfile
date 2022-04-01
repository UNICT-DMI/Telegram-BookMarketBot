FROM python:3.9-slim
WORKDIR /app

RUN apt-get update && apt-get -y install gcc libffi-dev

COPY requirements.txt .
#Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

#Start the bot
ENTRYPOINT [ "python3", "main.py" ]