FROM python:3.8-bullseye

RUN apt-get update && apt-get install -y sox normalize-audio libsndfile1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .

EXPOSE 8000
CMD python manage.py collectstatic --noinput --clear && \
  gunicorn SuiSiannAdmin.wsgi \
  -b 0.0.0.0:8000 \
  --timeout 120 \
  --log-level debug
