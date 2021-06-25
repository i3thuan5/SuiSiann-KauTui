FROM python:3.8-buster AS tsiantuan

RUN apt-get update && apt-get install -y sox normalize-audio

RUN mkdir djangoAdmin
WORKDIR djangoAdmin
COPY requirements.txt .
RUN pip install -r ./requirements.txt
RUN pip install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
COPY . .

RUN cat ./SuiSiannAdmin/docker_tsuki.py >> ./SuiSiannAdmin/settings.py
RUN python manage.py collectstatic

FROM nginx:1-alpine

COPY ./nginx/default.conf /etc/nginx/conf.d
COPY --from=tsiantuan /static/ /user/share/nginx/html/static/
