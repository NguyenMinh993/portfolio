# Use Python 3.10
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Run migrations and start gunicorn with Railway's PORT
CMD python manage.py migrate && gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 3 DjangoProject.wsgi:application
