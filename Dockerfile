# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables for Python (recommended)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies (if needed)
RUN pip install poetry

# Copy only the pyproject.toml and poetry.lock files to leverage Docker cache
COPY pyproject.toml poetry.lock /app/

# Install project dependencies using Poetry within a virtual environment
RUN poetry config virtualenvs.create true && \
    poetry install --no-dev

# Copy the rest of the application code into the container
COPY src/ /app/src/

# Expose the port on which your Django app will run (e.g., 8000)
EXPOSE 8000

# Start the Django development server within the virtual environment
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]