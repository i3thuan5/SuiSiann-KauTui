FROM python:3.7
MAINTAINER a8568730

RUN mkdir djangoAdmin
WORKDIR djangoAdmin
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .

CMD python manage.py runserver 0.0.0.0:8000

