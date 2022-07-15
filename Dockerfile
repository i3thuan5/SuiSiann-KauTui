FROM python:3.8-buster

RUN apt-get update && apt-get install -y sox normalize-audio libsndfile1

RUN mkdir djangoAdmin
WORKDIR djangoAdmin
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .

EXPOSE 8000
CMD gunicorn SuiSiannAdmin.wsgi \
  -b 0.0.0.0:8000 \
  --log-level debug

