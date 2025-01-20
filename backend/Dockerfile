# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the entire backend folder into the container
COPY . /app

# Copy only requirements first to leverage Docker caching
COPY class_api/requirements.txt /app/class_api/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/class_api/requirements.txt

# Set environment variable for the configuration file path
ENV MLFLOW_CONFIG_PATH=/app/backend/classification/mlflow_config.yaml

# Expose the application port
EXPOSE $PORT

# Run the application
CMD [ "python", "-m", "class_api.app" ]



















# FROM python:3.10

# WORKDIR /app

# COPY . /app
# RUN pip install --upgrade pip
# RUN pip install -r /app/class_api/requirements.txt


# EXPOSE $PORT

# CMD [ "python", "-m", "class_api.app" ]


# CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:$PORT", "class_api.app:app"]