FROM python:3

RUN mkdir /app
WORKDIR /app

COPY . /app

COPY requirements.txt  /app

RUN pip install --no-cache-dir -r requirements.txt


RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
