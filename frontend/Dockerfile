FROM 695523369539.dkr.ecr.eu-west-1.amazonaws.com/python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV API_HOSTNAME=backend-server
ENV PORT =8000
ENV API_PORT=8001

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]