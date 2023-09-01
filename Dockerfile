# Use the python latest image
FROM python:3.11

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Copy the current folder content into the docker image
COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Bind the port and refer to the app.py app
CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 main:app
