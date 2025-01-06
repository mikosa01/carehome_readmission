FROM python:3.10

WORKDIR /app

COPY class_api /app/
COPY classification /app/

RUN pip --no-cache-dir -r  app/classification/requirements.txt
RUN pip --no-cache-dir -r app/class_api/requirements.txt

EXPOSE 5000

CMD [ "python", '/app/class_api/app.py' ]