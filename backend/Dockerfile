FROM python:3.10
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /api

COPY  . /api/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001
CMD [ "python","manage.py","runserver","0.0.0.0:8001" ]