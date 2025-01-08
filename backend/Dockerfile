FROM python:3.10

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install -r /app/class_api/requirements.txt


EXPOSE 5000

CMD [ "python", '/app/class_api/app.py' ]