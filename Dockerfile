FROM python:3.6.4
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app
CMD python manage.py run -h 0.0.0.0
