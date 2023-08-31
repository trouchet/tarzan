# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables for Python (recommended)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies (if needed)
RUN pip install poetry Django

# Copy only the pyproject.toml and poetry.lock files to leverage Docker cache
COPY pyproject.toml poetry.lock manage.py /app/

# Install project dependencies
RUN poetry install

# Copy the rest of the application code into the container
COPY src/ /app/src/

# Expose the port on which your Django app will run (e.g., 8000)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]