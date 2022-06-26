FROM python:3.7


CMD ["python3", "--version"]
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./RzakaCH .

RUN apt-get update ##[edited]

CMD python3 bot.py
