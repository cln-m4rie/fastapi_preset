FROM python:3.7-slim

RUN pip install -U pip
RUN pip install pipenv

ADD Pipfile /var/www/html/
ADD Pipfile.lock /var/www/html/

RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
RUN rm requirements.txt

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80"]