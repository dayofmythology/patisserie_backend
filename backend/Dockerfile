FROM 695523369539.dkr.ecr.eu-west-1.amazonaws.com/python:3.10
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT=8001
WORKDIR /api

COPY  . /api/

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
CMD [ "python","manage.py","runserver","0.0.0.0:8001" ]