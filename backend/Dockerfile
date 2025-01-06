FROM python:3.10

WORKDIR /app

COPY class_api /app/
COPY classification /app/

RUN ls -l /app/class_api/requirements.txt  # Check if the file is copied correctly
RUN pip install -r /app/class_api/requirements.txt


EXPOSE 5000

CMD [ "python", '/app/class_api/app.py' ]