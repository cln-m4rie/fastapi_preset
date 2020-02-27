FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y
RUN apt-get install -y tzdata
RUN echo "Asia/Tokyo" >  /etc/timezone

RUN pip install -U pip
RUN pip install pipenv

ADD Pipfile /
ADD Pipfile.lock /

RUN pipenv lock -r > requirements.txt
RUN apt-get install -y g++ make default-libmysqlclient-dev default-mysql-client
RUN pip install -r requirements.txt --no-cache-dir
RUN rm requirements.txt
RUN rm -rf /tmp/* /var/tmp/*
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80"]
