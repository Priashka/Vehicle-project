# Use the official Python image
FROM python:3.11-slim

# Set environment variables to keep Python from buffering and creating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for PostgreSQL (psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project code into the container
COPY . /app/

# Expose the port Django runs on
EXPOSE 8000

# Start the application using Gunicorn (production server)
CMD python manage.py migrate && python create_admin.py && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT