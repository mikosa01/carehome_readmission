FROM python:3.10

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install -r /app/class_api/requirements.txt


EXPOSE $PORT

# CMD [ "python", '/app/class_api/app.py' ]

# CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:$PORT", "class_api.app:app"]