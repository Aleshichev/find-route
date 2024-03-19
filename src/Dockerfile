
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend_app
WORKDIR /backend_app

COPY . .

RUN pip install -U pip 
RUN pip install -r requirements.txt
# FROM python:alpine

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /usr/src/find_route

# COPY ./requirements.txt /usr/src/requirements.txt
# RUN pip install -r /usr/src/requirements.txt

# COPY . /usr/src/find_route

# EXPOSE 8000
# #CMD ["pyhon",  "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# FROM python:alpine

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /usr/src/find_route

# COPY ./requirements.txt /usr/src/requirements.txt
# RUN pip install -r /usr/src/requirements.txt

# COPY . /usr/src/find_route


# EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "find_route.travel.wsgi:application"]

