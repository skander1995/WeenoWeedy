From python:3.9.10


COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . code
WORKDIR /code

EXPOSE 9900

# ENTRYPOINT ['python', 'manage.py']
# CMD ['runserver' ,"0.0.0.0:9900"]
#pip install django-environ