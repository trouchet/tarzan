# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables for Python (recommended)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies (if needed)
RUN pip install poetry

# Copy only the project files needed initially
COPY . /app/
COPY scripts/django-utils.sh /app/

# Set executable permissions for the script
RUN chmod +x /app/django-utils.sh

# Install project dependencies using Poetry within a virtual environment
RUN poetry config virtualenvs.create true && \
    poetry install --no-dev

# Expose the port on which your Django app will run (e.g., 8000)
EXPOSE 8000

# Start the Django development server within the virtual environment
# Run database migrations and collect static files before starting the Django app
CMD ["./django-utils.sh"]


