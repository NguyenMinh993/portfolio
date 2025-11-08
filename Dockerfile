# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose port
EXPOSE 8000

# Run collectstatic
RUN python manage.py collectstatic --noinput

# Run gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "DjangoProject.wsgi:application"]
